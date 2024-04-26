import argparse
import sys
sys.path.append('/share/home/zju0019844/.conda/envs/dkly/Learn-Bert-Again/code')  # Replace '/path/to/parent/directory' with the actual path

import roberta  # Assuming roberta.py is inside the 'code' folder

# Define and parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--model_type", type=str, help="Model type.")
parser.add_argument("--model_name_or_path", type=str, help="Path to pre-trained model or shortcut name.")
parser.add_argument("--do_train", action='store_true', help="Whether to run training.")
parser.add_argument("--do_eval", action='store_true', help="Whether to run eval on the dev set.")
parser.add_argument("--do_test", action='store_true', help="Whether to run testing.")
parser.add_argument("--data_dir", type=str, help="The input data dir.")
parser.add_argument("--output_dir", type=str, help="The output directory where the model predictions and checkpoints will be written.")
parser.add_argument("--max_seq_length", type=int, default=1024, help="The maximum total input sequence length after tokenization.")
parser.add_argument("--split_num", type=int, default=1, help="The number of splits for the input.")
parser.add_argument("--lstm_hidden_size", type=int, default=512, help="Hidden size for LSTM.")
parser.add_argument("--lstm_layers", type=int, default=2, help="Number of layers for LSTM.")
parser.add_argument("--lstm_dropout", type=float, default=0.1, help="Dropout for LSTM.")
parser.add_argument("--eval_steps", type=int, default=500, help="Run evaluation every X steps.")
parser.add_argument("--per_gpu_train_batch_size", type=int, default=4, help="Batch size per GPU/CPU for training.")
parser.add_argument("--gradient_accumulation_steps", type=int, default=4, help="Number of updates steps to accumulate before performing a backward/update pass.")
parser.add_argument("--warmup_steps", type=int, default=0, help="Linear warmup over warmup_steps.")
parser.add_argument("--per_gpu_eval_batch_size", type=int, default=32, help="Batch size per GPU/CPU for evaluation.")
parser.add_argument("--learning_rate", type=float, default=5e-6, help="The initial learning rate for Adam.")
parser.add_argument("--adam_epsilon", type=float, default=1e-6, help="Epsilon for Adam optimizer.")
parser.add_argument("--weight_decay", type=float, default=0, help="Weight decay if we apply some.")
parser.add_argument("--train_steps", type=int, default=10000, help="Total number of training steps to perform.")
parser.add_argument("--freeze", type=int, default=0, help="Freeze the encoder layers up to this number.")
parser.add_argument("--hidden_size", type=int, default=1024, help="Hidden size for the linear layer.")
parser.add_argument("--num_labels", type=int, default=3, help="Number of labels for classification task.")
parser.add_argument("--num_layers", type=int, default=1, help="Number of layers for the linear layer.")
parser.add_argument("--dropout", type=float, default=0.1)
args = parser.parse_args()

# Call the main function with parsed arguments
roberta.main(args=args)



