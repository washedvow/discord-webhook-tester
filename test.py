from dhooks import Webhook, Embed

hook_get = input("what is your webhook?")
hook = Webhook(hook_get)

embed = Embed( 
    description='a webhook tester developed by vow :heart:',
    color=0x6BFF33,
    timestamp='now'
    )
embed.set_author(name='What is this? ')
embed.set_footer(text='vow webhook tester')


hook.send(embed=embed)



print('                                                              ')
print('                                                              ')
print('                                                              ')

print('Hook Sent!')