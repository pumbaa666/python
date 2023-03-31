# http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application 

#export FLASK_DEBUG=1 # If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.
#export FLASK_APP=main.py #pour que flask run sache quoi lancer



if [ -z "$1" ]; then
	echo "No argument, try to run last program"
else
	if [[ $1 == *.py ]]; then
		export FLASK_APP="$1"
	else
		export FLASK_APP="$1".py
	fi
fi
echo "DEBUG : FLASK_APP = "$FLASK_APP

if [ -z "$2" ]; then
	export FLASK_DEBUG=1
else
	export FLASK_DEBUG=$2
fi
echo "DEBUG : debugging = $FLASK_DEBUG (1 = enabled, 0 = disabled)"

if [ -z "$3" ]; then
	export PARAM="--host=0.0.0.0" # pour que le serveur soit accessible depuis une autre machine
else
	export PARAM="$3"
fi
echo "DEBUG : Param = $PARAM"

#flask run
#python -m flask run $PARAM #juste une alternative
flask run $PARAM

