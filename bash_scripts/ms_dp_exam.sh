# to run script go with:
# bash search.sh "Fiscal"
word="$1"
echo "searching for ${word}"
echo
cd C:\VSbranch

for dir in *dbt-*; do
    if [ -d "$dir" ]; then
        cd "$dir"
	echo "$dir"
        git checkout develop > /dev/null 2>&1
	git pull > /dev/null 2>&1
	grep -i -r -o $word . | uniq -c # ignoring string case, recurence searching, match only, count unique values
	echo
        cd ..
    fi
done
