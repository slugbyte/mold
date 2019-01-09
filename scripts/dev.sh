# setup bash environment vars and a dev MOLD_ROOT_ROOT
export MOLD_ROOT=$HOME/.mold-dev
export MOLD_DEBUG='true'
export MOLD_COLOR='true'
alias mold="python3 -m mold"
alias less='less -r'
alias clean_mold='rm -rf build mold.egg-info mold/__pycache__ dev-root'

_mold(){
  MOLD_COMPLETE=$(mold complete $COMP_LINE) 
  if [[ $MOLD_COMPLETE == '__MAGIC_MOLD__' ]]; then 
      # MAGIC_MOLD turns off COMPREPLY so the shell will allow 
      # normal file path completeion
      #echo 'boom' $canidate
    for canidate in $(compgen -f $2); do 
      if [[ "$canidate" == "$2"* ]];then
        COMPREPLY+=("$canidate")
      fi 
    done
  else 
    for canidate in $MOLD_COMPLETE; do 
      if [[ "$canidate" == "$2"* ]];then
        COMPREPLY+=("$canidate")
      fi 
    done
  fi
}
complete -F _mold mold
