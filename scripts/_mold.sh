_mold(){
  for canidate in $(mold complete $COMP_LINE); do 
    if [[ "$canidate" == "$2"* ]];then
      COMPREPLY+=("$canidate")
    fi
  done
}

complete -F _mold mold
