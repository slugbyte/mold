# setup bash environment vars and a dev MOLD_ROOT_ROOT
export MOLD_ROOT=$PWD/dev-root
export MOLD_DEBUG_MODE='true'
alias mold="python3 -m mold"
alias clean_mold='rm -rf build mold.egg-info mold/__pycache__ dev-root'
mkdir -p $MOLD_ROOT/conf $MOLD_ROOT/pack $MOLD_ROOT/drop $MOLD_ROOT/temp $MOLD_ROOT/plug

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
echo 'loaded dev'
