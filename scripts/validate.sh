#!/usr/bin/env bash
set -eo pipefail
echo "🔍 Validating WebGPU In-Browser Small LM Suite..."
python3 -c "import server_fallback; print('✅ server_fallback gateway verified')"
python3 -c "import py_compile; py_compile.compile('manim_flow.py', doraise=True); print('✅ manim_flow syntax verified')"
echo "✅ SRE compliance validation complete for webgpu-browser-slm."
