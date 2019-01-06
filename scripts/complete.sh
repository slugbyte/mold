_dot(){
  for canidate in $(dot complete $COMP_LINE); do 
    if [[ "$canidate" == "$2"* ]];then
      COMPREPLY+=("$canidate")
    fi
  done
}

complete -F _dot dot
