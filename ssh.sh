if [ $1 = gen ]; then 
  openssl rand -base64 $3 > passwords/$2.txt
fi
if [ $1 = conn ]; then
  ssh $2
fi
if [ $1 = add ]; then
  echo $2 > passwords/$3.txt
fi
if [ $1 = read ]; then
  cat passwords/$2.txt
fi
