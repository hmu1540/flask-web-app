###options of values of properties

recurrence 'one time only'(0) | 'long-term'(1)

    time_commitment: 'a few minutes'(0) | 'a few hours'(1) | 'a few days'(2)

recurrence  'long-term'

    time_commitment:  "a few hours per week"(0) | "a few hours per month"(1) | "part time"(2) | "full time"(3)

schedule "weekdays"(0), "weekends"(1)

virtual: no(0), yes(1)
virtual_where: <option value="WORLD">Volunteer can be anywhere in the world</option>
<option value="COUNTRY">Volunteer must be in a certain country</option>
<option value="CITY">Volunteer must be in a certain city or town</option>

action_type:  ## volunteer, job, internship