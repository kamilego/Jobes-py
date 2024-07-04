# bash ms_dp_exam.sh 1 1 10
# topic 1 limit of questions 114

topic=$1
for ((num=$2; num<=$3; num++))
do
        exam_url=$(grep -o "https://www.examtopics.com/discussions/microsoft/view/.*-exam-dp-203-topic-${topic}-question-${num}-discussion/" dp_exam_url.txt)
        if [ -n "$exam_url" ]; then
		start chrome $exam_url
        else
                echo "Could not find topic: ${topic} question: ${num}"
	fi
done
