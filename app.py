import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '503973275:AAGy0lGGnAfmZmnYqGuyA47vPjoyjMD3XrU'
WEBHOOK_URL = 'https://91c0af44.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
		'state3',
		'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10'
    ],
    transitions=[
        {#user to state1
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {#state1 to state2
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {#state1 to state10
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
        {#state2 to state1
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {#state2 to state3
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {#state2 to state4
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {#state2 to state5
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {#state2 to state6
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {#state2 to state7
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {#state2 to state8
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {#state2 to state9
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
        {#state2 to user
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'user',
            'conditions': 'bye_to_user'
        },
        {#state1 to user
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'user',
            'conditions': 'bye_to_user'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state2',
            ],
            'dest': 'state1'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state10',
            ],
            'dest': 'state1'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state3',
                'state4',
                'state5',
                'state6',
                'state7',
                'state8',
                'state9',
            ],
            'dest': 'state2'
        }
        
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

if __name__ == "__main__":
    _set_webhook()
    machine.get_graph().draw('state_diagram.png', prog = 'dot')
    app.run()
