from dhooks import Webhook, Embed

hook_get = input("what is your webhook?")
hook = Webhook(hook_get)

embed = Embed( 
    description='a webhook tester developed by vow :heart:',
    color=0x6BFF33,
    timestamp='now'
    )

image1 = 'https://imgur.com/Whn4p8f.png'


embed.set_author(name='What is this? ')
embed.set_footer(text='vow webhook tester', icon_url=image1)


hook.send(embed=embed)



print('                                                              ')
print('                                                              ')
print('                                                              ')

print('Hook Sent!')