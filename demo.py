import fire
from lora import Llama_Lora, Gemma_Lora
from huggingface_hub import login

ACCESS_TOKEN= ""   #add access token
login(token=ACCESS_TOKEN)

def main(
        task: str = "eval",
        llm: str = "gemma",
        base_model: str = "google/gemma-7b-it",
):
    # base_model_name: str = "meta-llama/Llama-2-7b-hf"
    if len(base_model) == 0:
        raise ValueError("Please specify the base model.")
    if llm == "llama":
        m = Llama_Lora(
            base_model=base_model,
        )
    elif llm == "gemma":
        m = Gemma_Lora(
            base_model = base_model,
        )
    else:
        raise ValueError(f"Unrecognized llm name: {llm}")
    if task == "train":
        m.train(
            train_file = "data/arxiv/part1_2014-2018",
            output_dir = f"./ckp_sst_{llm}_lora",
            train_batch_size = 32,
            num_epochs = 1,
            group_by_length = False,
            logging_steps = 5,
            val_steps = 20,
            val_batch_size = 8,
        )
    elif task == "eval":
        m.predict(
            input_file = "data/sst2/val.json",
            # lora_adapter = "./ckp_sst2_llama2_lora",
            max_new_tokens = 32,
            verbose = True,
        )
    else:
        raise ValueError(f"Unknown model name: {base_model_name}")


if __name__ == "__main__":
    fire.Fire(main)