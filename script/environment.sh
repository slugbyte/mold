# setup bash environment vars and a dev MOLD_ROOT_ROOT
echo "Seting Enviornment variabels"
echo "    MOLD_ROOT: $HOME/mold-dev"
echo "    MOLD_DEBUG: true"
echo "    MOLD_COLOR: true"
export MOLD_ROOT=$HOME/.mold-dev
export MOLD_DEBUG='true'
export MOLD_COLOR='true'

echo "Creating aliases"
echo "    mold is now aliased to 'python3 -m mold'"
echo "    _mold_build is now aliased to 'python3 ./setup.py build'"
echo "    _mold_clean alias will delete build, mold.egg-info, __pycache dirs and $MOLD_ROOT"
alias mold="python3 -m mold"
alias _mold_clean='rm -rf build mold.egg-info mold/__pycache__'
alias _mold_build="python3 ./setup.py build"

_mold(){
  MOLD_COMPLETE=$(mold --complete $COMP_LINE) 
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

echo "Enabling tab completion"
complete -F _mold mold
