from flask import render_template, redirect, url_for, request, abort, session, flash


class Alert() :


    def set(icon = 'success', title = 'Success', text = 'Test') :
        session['iconFlash'] = icon
        session['titleFlash'] = title
        session['textFlash'] = text
        flash(icon, 'icon')
        flash(title, 'title')
        flash(text, 'text')

    def get():
        icon = session['iconFlash'] if 'iconFlash' in session else ''
        title = session['titleFlash'] if 'titleFlash' in session else ''
        text = session['textFlash'] if 'textFlash' in session else ''
        load = '<div id="flash" data-icon="' + icon + '" data-title="' + title + '" data-text="' + text + '" data-url=""></div>'
        print(load)
        return load