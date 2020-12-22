#!/usr/bin/env bash

function colorize() {
  local color type=0

  case $1 in
    black)
      color=30
      ;;
    red)
      color=31
      ;;
    green)
      color=32
      ;;
    yellow)
      color=33
      ;;
    blue)
      color=34
      ;;
    magenta)
      color=35
      ;;
    cyan)
      color=36
      ;;
    white)
      color=37
      ;;
    reset | *)
      color=0
      ;;
  esac

  case $2 in
    bold | bright)
      type=1
      ;;
    underline)
      type=4
      ;;
    inverse)
      type=7
      ;;
  esac

  echo -en "\\033[${type};${color}m"
}

function echo_error() {
  colorize red bold
  echo "ERROR:$(colorize reset)" "$@"
}

function echo_warning() {
  colorize yellow bold
  echo "WARNING:$(colorize reset)" "$@"
}

function echo_done() {
  colorize green bold
  echo "DONE:$(colorize reset)" "$@"
}

function echo_info() {
  if [ "$#" -eq 1 ]; then
    PREFIX="INFO"
  else
    PREFIX=$1
    shift 1
  fi

  colorize cyan bold
  echo "${PREFIX}:$(colorize reset)" "$@"
}

function not_installed() {
  [ ! -x "$(command -v "$@")" ]
}

function load_env() {
  ENV_FILE=${1:-.env}
  set -a
  if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE"
  else
    echo_error "Couldn't locate ${ENV_FILE} file..."
  fi
  set +a
}
