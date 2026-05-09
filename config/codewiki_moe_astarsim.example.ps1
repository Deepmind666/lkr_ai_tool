# Example CodeWiki setup for the MoE/Astra-Sim repository.
# Fill provider credentials with `codewiki config set` on the target machine.
# Do not commit API keys or generated private documentation.

codewiki config agent `
  --exclude ".git,.venv,venv,node_modules,build,dist,__pycache__,.cache,*.zip,*.tar,*.tar.gz,*.zst,*.npz,*.npy,*.pt,*.pth,*.safetensors,*.onnx,*.et,*.log,moe_runs,local_runs,artifacts/figures/**/figures,experiments/**/output*,experiments/**/results*,experiments/**/Stage1_collect/results" `
  --focus "MoE_Workload_Simulation,experiments/load_generator_v3,experiments/zys-chakra-convert,examples/workload/moe" `
  --doc-type architecture

codewiki config validate

# Run from the repository root after confirming `git status -sb` is understood:
# codewiki generate --output docs/codewiki --verbose
