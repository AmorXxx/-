#!/root
while :       #循环，为了让脚本一直运行监控
 do
  COUNT1=`ps -ef | grep jiaogonghao-pi.py |wc -l`
  if [ "$COUNT1" -gt 1 ];then
      echo "client service is ok"
  else
      echo "client servicie not exist"
      python3 jiaogonghao-pi.py
  fi
  sleep 60
 done

