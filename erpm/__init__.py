import collections

CredentialPlugin = collections.namedtuple('CredentialPlugin', ['name', 'inputs', 'backend'])

def get_password(**kwargs):
    #
    # IMPORTANT:
    # replace this section of code with Python code that *actually*
    # interfaces with some third party credential system
    # (*this* code is just provided for the sake of example)
    #
    url = kwargs.get('url')
    erpm_username = kwargs.get('erpm_username')
    erpm_password = kwargs.get('erpm_password')
    account_name = kwargs.get('account_name')
    shared_credential_list = kwargs.get('shared_credential_list')
    system_name = kwargs.get('system_name')


    if account_name != 'VALID':
        raise ValueError('Invalid Account!')
    if shared_credential_list != 'VALID':
        raise ValueError('Invalid shared_credential_list')
    if system_name != 'VALID':
        raise ValueError('Invalid system name')

    value = {
        'shared_credential_list': 'AnsibleSCL',
        'email': 'mary@example.org',
        'password': 'super-secret'
    }

    if shared_credential_list in value:
        return value[shared_credential_list]

    raise ValueError(f'Could not find a value for {shared_credential_list}.')

erpm_plugin = CredentialPlugin(
    'ERPM Credential Plugin',
    # see: https://docs.ansible.com/ansible-tower/latest/html/userguide/credential_types.html
    # inputs will be used to create a new CredentialType() instance
    #
    # inputs.fields represents fields the user will specify *when they create*
    # a credential of this type; they generally represent fields
    # used for authentication (URL to the credential management system, any
    # fields necessary for authentication, such as an OAuth2.0 token, or
    # a username and password). They're the types of values you set up _once_
    # in AWX
    #
    # inputs.metadata represents values the user will specify *every time
    # they link two credentials together*
    # this is generally _pathing_ information about _where_ in the external
    # management system you can find the value you care about i.e.,
    #
    # "I would like Machine Credential A to retrieve its username using
    # Credential-O-Matic B at identifier=some_key"
    inputs={
        'fields': [{
            'id': 'url',
            'label': 'ERPM Base URL',
            'type': 'string',
            'help_text': 'The Base URL of ERPM System.'
        },{
            'id': 'erpm_username',
            'label': 'ERPM Username',
            'type': 'string',
            'secret': True,
            'help_text': 'The Username to login to ERPM System.'
        },{
            'id': 'erpm_password',
            'label': 'ERPM Password',
            'type': 'string',
            'secret': True,
            'help_text': 'The Password to login to ERPM System.'
        },{
            'id': 'system_name',
            'label': 'System Name',
            'type': 'string',
            'help_text': 'The name of the System in ERPM to fetch password.'
        },{
            'id': 'account_name',
            'label': 'Account Name',
            'type': 'string',
            'help_text': 'The name of the Account in ERPM System to fetch password.'
        },{
            'id': 'shared_credential_list',
            'label': 'Shared Credential Liste',
            'type': 'string',
            'help_text': 'The name of the Shared Credential List in ERPM System to fetch.'
        },{
        'id' : 'comment',
        'label': 'Comment',
        }],
        #'metadata': [{
            #'id': 'shared_credential_list',
            #'label': 'Share Credential List Name',
            #'type': 'string',
            #'help_text': 'The name of the Shared Credential List in ERPM System to fetch.'
        #}],
        'required': ['url', 'username', 'password', 'account_name', 'shared_credential_list', 'system_name'],
    },
    # backend is a callable function which will be passed all of the values
    # defined in `inputs`; this function is responsible for taking the arguments,
    # interacting with the third party credential management system in question
    # using Python code, and returning the value from the third party
    # credential management system
    backend = get_password
)
