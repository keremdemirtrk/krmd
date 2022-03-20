from cement import Controller, ex
from time import strftime



class Commands(Controller):
    class Meta:
        label = 'commands'
        stacked_type = 'embedded'
        stacked_on = 'base'
    
    @ex(help='list command')
    def list(self):
        data = {}
        data['commands'] = self.app.db.all()
        self.app.render(data, 'commands/list.jinja2')
        
    @ex(
        help='add new command',
        arguments=[
            (  ['command_text'],
               {'help': 'krmd command text',
                'action': 'store'}
            ),
        ],    
    )

    def add(self):
        text = self.app.pargs.command_text
        now = strftime("%Y-%m-%d %H:%M:%S")
        self.app.log.info('creating commands: %s' % text)

        command = {
            'timestamp': now,
            'text': text,
        }

        self.app.db.insert(command)

    @ex(
        help='update an existing command',
        arguments=[
            ( ['command_id'],
              {'help': 'command database id',
               'action': 'store' } ),
            ( ['command_text'],
              {'help': 'command text',} ),
        ],
    )
    def update(self):
        id = int(self.app.pargs.command_id)
        text = self.app.pargs.command_text
        now = strftime("%Y-%m-%d %H:%M:%S")
        self.app.log.info('updating command: %s - %s' % (id, text))

        command = {
            'timestamp': now,
            'text': text,
        }

        self.app.db.update(command, doc_ids=[id])
    
    @ex(
        help='delete a command',
        arguments=[
            (['command_id'],
            {'help': 'command database id',
             'action': 'store'}),
        ],
        )
    def delete(self):
        id = int(self.app.pargs.command_id)
        self.app.db
        self.app.log.info('deleting command: %s' % id)
        self.app.db.remove(doc_ids=[id])
        
    