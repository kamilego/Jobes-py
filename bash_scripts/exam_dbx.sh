for ((num=$1; num<=$2; num++))
do
	start chrome https://www.google.com/search?q=examtopics+Exam+Certified+Data+Engineer+Associate+topic+1+question+${num}
	sleep 1
done
