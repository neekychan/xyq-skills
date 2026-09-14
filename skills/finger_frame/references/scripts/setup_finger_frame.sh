#!/usr/bin/env bash
# finger_frame 环境引导：幂等安装 mediapipe 及视觉依赖，探针通过输出 SETUP_OK。
# 设计要点：
# - 统一 python3 -m pip，防 pip3 绑定到其他解释器。
# - --break-system-packages 仅 pip>=23.0.1 支持（线上沙箱实测 pip 22.0.2 会报
#   no such option），先探测能力再按需追加；非 PEP668 环境裸装失败时退 --user。
# - 沙箱 pip 默认走内部镜像（PIP_INDEX_URL=bytedpypi），实测缺 mediapipe 包——
#   失败时显式 --index-url 切源重试（命令行优先级盖过环境变量），链路：
#   内部镜像 → 中科大 USTC（国内快）→ pypi.org 官方（沙箱实测可达 200，最终兜底）。
#   注：TUNA 被沙箱出网策略拦（返回拦截页致 from versions: none），不用。
# - --no-deps 装 mediapipe，绕开 sounddevice(需 PortAudio 系统库) 与
#   opencv-contrib-python(需 libGL)；视觉链路手动补 headless 依赖集。
# - 模型 hand_landmarker.task 随 skill 打包，不做在线下载。
# - pip 全部输出落 /tmp 日志，SETUP_FAIL 时带出末行供诊断。
set -u

PIP_PKGS="opencv-python-headless numpy matplotlib pillow flatbuffers protobuf absl-py"
PIP_LOG="/tmp/finger_frame_pip.log"
PIP="python3 -m pip"
PYPI_USTC="--index-url https://mirrors.ustc.edu.cn/pypi/simple"
PYPI_OFFICIAL="--index-url https://pypi.org/simple"

BSP=""
$PIP install --help 2>/dev/null | grep -q -- --break-system-packages && BSP="--break-system-packages"

probe() {
  python3 -c "import mediapipe; from mediapipe.tasks.python import vision; print(mediapipe.__version__)" 2>/dev/null
}

VER="$(probe)"
if [ -z "$VER" ]; then
  : > "$PIP_LOG"
  $PIP install --quiet $BSP $PIP_PKGS >>"$PIP_LOG" 2>&1 \
    || $PIP install --quiet $BSP $PYPI_USTC $PIP_PKGS >>"$PIP_LOG" 2>&1 \
    || $PIP install --quiet $BSP $PYPI_OFFICIAL $PIP_PKGS >>"$PIP_LOG" 2>&1
  $PIP install --quiet $BSP --no-deps mediapipe >>"$PIP_LOG" 2>&1 \
    || $PIP install --quiet $BSP --no-deps $PYPI_USTC mediapipe >>"$PIP_LOG" 2>&1 \
    || $PIP install --quiet $BSP --no-deps $PYPI_OFFICIAL mediapipe >>"$PIP_LOG" 2>&1
  VER="$(probe)"
fi

MODEL="$(dirname "$0")/models/hand_landmarker.task"
if [ -n "$VER" ] && [ -f "$MODEL" ]; then
  echo "SETUP_OK mediapipe=$VER model=$MODEL"
elif [ -z "$VER" ]; then
  echo "SETUP_FAIL reason=mediapipe-import pip=[$($PIP --version 2>/dev/null | head -1)] log_tail=[$(tail -3 "$PIP_LOG" 2>/dev/null | tr '\n' ' ')]"
  exit 1
else
  echo "SETUP_FAIL reason=model-missing path=$MODEL"
  exit 1
fi
