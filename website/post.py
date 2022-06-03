from flask import Blueprint, request, flash, redirect, url_for
from flask.templating import render_template

from website.auth import login_required
import website.post_automation # post_automation script implementing automatic posting of postions

post = Blueprint("post", __name__, '/post')

@post.route('/result')
def result():
    return render_template('post/result.html') # validate successfull posting? 

@post.route('/create', methods=('POST', 'GET'))
@login_required
def create():
    if request.method == 'POST':
        username = request.form['username']
        password= request.form['password']
        title = request.form['title']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        # hard coding for experiments
        event_kind = "volunteer"
        event_type = "multiday"
        start_hour= "12"
        start_min= "00"
        start_ampm= "am"
        end_date= "07/08/2022"
        end_hour= "11"
        end_min= "59"
        end_ampm= "pm"
        recurrence=1
        time_commitment= 0
        schedule= 1
        timezone= "Chicago"
        virtual= 1
        virtual_where= "COUNTRY"
        action_type= "VOLOP"
        # end experiments


        error = None

        if not (title and description) :
            error = "* field is required."
        if error:
            flash(error)
        else:
            
            """ Call from post_automation.py """

            give_pulse = website.post_automation.GivePulse()
            give_pulse.publish(username = username,
                                password = password,
                                title = title,
                                event_kind = event_kind,
                                event_type = event_type,
                                description = description,
                                start_date = start_date,
                                start_hour = start_hour,
                                start_min = start_min,
                                start_ampm = start_ampm,
                                end_date = end_date,
                                end_hour = end_hour,
                                end_min = end_min,
                                end_ampm = end_ampm,
                                recurrence = recurrence,
                                time_commitment = time_commitment,
                                schedule = schedule,
                                timezone = timezone,
                                virtual = virtual,
                                virtual_where = virtual_where,
                                action_type = action_type
                                )
            # if the post is published, then
            return redirect(url_for('post.result'))

    return render_template('post/create.html')

