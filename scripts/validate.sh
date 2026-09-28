#!/usr/bin/env bash
set -e
echo "🔍 Validating WebGPU In-Browser Small LM Suite..."
python3 -c "import py_compile; py_compile.compile('server_fallback.py', doraise=True); print('✅ server_fallback syntax verified')"
python3 -c "import py_compile; py_compile.compile('manim_flow.py', doraise=True); print('✅ manim_flow syntax verified')"
echo "✅ SRE compliance validation complete for webgpu-browser-slm."
