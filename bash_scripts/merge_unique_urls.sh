cat url*.txt | sort -u | sort -t '-' -k6,6n -k8,8n -o urls_exam.txt
# split main exam chars in url
# echo "$a" | tr "/" "-" | grep -Po "\-\d+\-" | tr "\n" " " | tr -d "-"
