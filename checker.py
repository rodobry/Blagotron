from discord.ext import commands
import discord.utils

def is_owner_check(message):
    return message.author.id == '132914536700182528'

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

def is_mod_or_admin():
    def predicate(ctx):
        return check_roles(ctx, lambda r: r.name in ('Blagosbire', 'Admin'))
    return commands.check(predicate)


def check_roles(ctx, check):
    msg = ctx.message
    if is_owner_check(msg):
        return True
    author = msg.author
    role = discord.utils.find(check, author.roles)
    return role


# The permission system of the bot is based on a "just works" basis
# You have permissions and the bot has permissions. If you meet the permissions
# required to execute the command (and the bot does as well) then it goes through
# and you can execute the command.
# If these checks fail, then there are two fallbacks.
# A role with the name of Bot Mod and a role with the name of Bot Admin.
# Having these roles provides you access to certain commands without actually having
# the permissions required for them.
# Of course, the owner will always be able to execute commands.

def check_permissions(ctx, perms):
    msg = ctx.message
    if is_owner_check(msg):
        return True

    ch = msg.channel
    author = msg.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())

def role_or_permissions(ctx, check, **perms):
    if check_permissions(ctx, perms):
        print (perms)
        return True

    ch = ctx.message.channel
    author = ctx.message.author
    if ch.is_private:
        return False # can't have roles in PMs

    role = discord.utils.find(check, author.roles)
    return role is not None

def mod_or_permissions(**perms):
    def predicate(ctx):
        return role_or_permissions(ctx, lambda r: r.name in ('Blagosbire', 'Admin'), **perms)

    return commands.check(predicate)

def admin_or_permissions(**perms):
    def predicate(ctx):
        return role_or_permissions(ctx, lambda r: r.name == 'Admin', **perms)

    return commands.check(predicate)