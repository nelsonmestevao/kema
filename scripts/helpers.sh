#!/usr/bin/env bash

VERSION=0.2.2

tput sgr0
RED=$(tput setaf 1)
ORANGE=$(tput setaf 3)
GREEN=$(tput setaf 2)
PURPLE=$(tput setaf 5)
CYAN=$(tput setaf 4)
BLUE=$(tput setaf 6)
WHITE=$(tput setaf 7)
BOLD=$(tput bold)
RESET=$(tput sgr0)

function log() {
  local LABEL="$1"
  local COLOR="$2"
  shift 2
  local MSG=("$@")
  printf "[${COLOR}${BOLD}${LABEL}${RESET}]%*s" $(($(tput cols) - ${#LABEL} - 2)) | tr ' ' '='
  for M in "${MSG[@]}"; do
    let COL=$(tput cols)-2-${#M}
    printf "%s%${COL}s${RESET}" "* $M"
  done
  printf "%*s\n" $(tput cols) | tr ' ' '='
}

function log_error() {
  log "FAIL" "$RED" "$@"
}

function log_warn() {
  log "WARN" "$ORANGE" "$@"
}

function log_success() {
  log "OK" "$GREEN" "$@"
}

function log_info() {
  local LABEL="INFO"

  if ! [ "$#" -eq 1 ]; then
    LABEL=$(echo "$1" | tr [a-z] [A-Z])
    shift 1
  fi

  log "${LABEL}" "$CYAN" "$@"
}

function help_section() {
  local TITLE=$(echo "$@" | tr [a-z] [A-Z])
  echo -e "${BOLD}${TITLE}${RESET}"
}

function load_env() {
  local ENV_FILE=${1:-.env}
  set -a
  if [ -f "$ENV_FILE" ]; then
    . "$ENV_FILE"
  else
    echo_error "Couldn't locate ${ENV_FILE} file..."
  fi
  set +a
}

function not_installed() {
  [ ! -x "$(command -v "$@")" ]
}

function display_version() {
    local program="$1"
    local version="$2"
    if not_installed figlet; then
      echo "${program} script version ${version}"
    else
      echo -n "${BLUE}${BOLD}"
      figlet "${program} script"
      echo -n "${RESET}"
      echo "version ${version}"
    fi
}
