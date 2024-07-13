# bash ms_dp_exam.sh 1 1 10
# topic 1 limit of questions 114 - missing 13,66,105
# topic 2 limit of questions 133 - missing 11
# topic 3 limit of questions 39  - missing 8
# topic 4 limit of questions 67  - no missings

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
