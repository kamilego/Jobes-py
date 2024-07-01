# bash ms_dp_exam.sh 1 1 10
# topic 1 limit of questions 114

topic=$1
for ((num=$2; num<=$3; num++))
do
        curl -s "https://www.google.com/search?q=examtopics+dp+203+topic+${topic}+question+${num}" -o temp1.txt
        grep -o -P ".{0,400}Exam DP-203 topic ${topic} question ${num} discussion" temp1.txt > temp2.txt
        exam_url=$(grep -o "https://www.examtopics.com/discussions/microsoft/view/.*-discussion/" temp2.txt)
        if [ -n "$exam_url" ]; then
                if [[ $(grep -L "$exam_url" exam_urls.txt) ]]; then
                        echo "$exam_url" >> exam_urls.txt
                fi
                start chrome "$exam_url"
        else
                echo "Could not find topic: ${topic} question: ${num}"
        fi
        rm temp*.txt
done
sort -t '-' -k6,6n -k8,8n exam_urls.txt -o exam_urls.txt
