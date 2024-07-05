# bash exam.sh 1 1 10
topic=$1
for ((num=$2; num<=$3; num++))
do
	start chrome "https://www.google.com/search?q=examtopics+dp+203+topic+${topic}+question+${num}"
done 
