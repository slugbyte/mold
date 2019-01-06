# setup bash environment vars and a dev MOLD_ROOT_ROOT
export MOLD_ROOT=$PWD/dev-root
export MOLD_DEBUG_MODE='true'
alias mold="python3 -m mold"
mkdir -p $MOLD_ROOT/conf $MOLD_ROOT/pack $MOLD_ROOT/drop $MOLD_ROOT/temp $MOLD_ROOT/plug

_mold(){
  for canidate in $(mold complete $COMP_LINE); do 
    if [[ "$canidate" == "$2"* ]];then
      COMPREPLY+=("$canidate")
    fi
  done
}
complete -F _mold mold
