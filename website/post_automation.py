from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from enum import Enum

## install sin shell ##
# pip install selenium

## Start the session ## 

# driver = webdriver.Firefox(profile)

""" 
Note: locator types can be ID, NAME, absolute XPATH, and relative XPATH. 
ID and NAME are better practice since they are constant while absolute XPATH can change and relative XPATH is slow to retrieve. 
We only apply XPATH when there are neither ID nor Name properties associated. 
"""

class Website:
    def __init__(
        self,
        URL="",
        login_username_locator=(),
        login_password_locator=(),
        login_submit_locator=(),
        form_link_locator=(),
        post_title_locator=(),
        post_evenkind_locator=(),
        post_eventtype_locator=(),
        post_description_frame_locator=(),
        post_description_locator=(),
        post_event_start_date_select_locator=(),
        post_event_start_hour_locator=(),
        post_event_start_min_locator=(),
        post_event_start_ampm_locator=(),
        post_event_end_date_select_locator=(),
        post_event_end_hour_locator=(),
        post_event_end_min_locator=(),
        post_event_end_ampm_locator=(),
        form_submit_locator=(),
    ) -> None:

        # element locators: child website-specific
        self.website = URL
        self.login_username_locator = login_username_locator
        self.login_password_locator = login_password_locator
        self.login_submit_locator = login_submit_locator
        self.form_link_locator = form_link_locator
        self.post_title_locator = post_title_locator
        self.post_evenkind_locator = post_evenkind_locator
        self.post_eventtype_locator = post_eventtype_locator
        self.post_description_frame_locator = post_description_frame_locator
        self.post_description_locator = post_description_locator
        self.post_event_start_date_select_locator = post_event_start_date_select_locator
        self.post_event_start_hour_locator = post_event_start_hour_locator
        self.post_event_start_min_locator = post_event_start_min_locator
        self.post_event_start_ampm_locator = post_event_start_ampm_locator
        self.post_event_end_date_select_locator = post_event_end_date_select_locator
        self.post_event_end_hour_locator = post_event_end_hour_locator
        self.post_event_end_min_locator = post_event_end_min_locator
        self.post_event_end_ampm_locator = post_event_end_ampm_locator
        self.form_submit_locator = form_submit_locator

        ## post info: fixed across child website
        self.username = ""
        self.password = ""
        self.title = ""
        self.event_kind = ""
        self.event_type = ""
        self.description = ""
        self.start_date = ""
        self.start_hour = ""
        self.start_min = ""
        self.start_ampm = ""
        self.end_date = ""
        self.end_hour = ""
        self.end_min = ""
        self.end_ampm = ""
        self.recurrence = ""
        self.time_commitment = ""
        self.schedule = ""
        self.timezone = ""
        self.virtual = ""
        self.virtual_where = ""
        self.action_type = ""

    def _start_session(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("geo.enabled", False)
        self.driver = webdriver.Firefox(profile)
        
    def _login(self):
        self.driver.fullscreen_window()
        self.driver.find_element(
            self.login_username_locator[0], self.login_username_locator[1]
        ).send_keys(self.username)
        self.driver.find_element(
            self.login_password_locator[0], self.login_password_locator[1]
        ).send_keys(self.password)
        self.driver.find_element(
            self.login_submit_locator[0], self.login_submit_locator[1]
        ).click()
        sleep(5)  # Wait until next page can load sucessfully

    def _open_form(self):
        self.driver.find_element(
            self.form_link_locator[0], self.form_link_locator[1]
        ).click()

    def _enter_form(self) -> None:
        # post title #
        self.driver.find_element(
            self.post_title_locator[0], self.post_title_locator[1]
        ).send_keys(self.title)

    def _save_form(self):
        self.driver.find_element(
            self.form_submit_locator[0], self.form_submit_locator[1]
        ).click()
        sleep(5)  # Wait until next page can load sucessfully

    def _publish(self):
        
        self._login()
        self._open_form()
        self._enter_form()
        self._save_form()

    def _close_session(self):
        sleep(15) # wait until the post can be succefully published
        self.driver.quit() # close session

    def publish(self, 
        username="",
        password="",
        title="",
        event_kind="",
        event_type="",
        description="",
        start_date="",
        start_hour="",
        start_min="",
        start_ampm="",
        end_date="",
        end_hour="",
        end_min="",
        end_ampm="",
        recurrence="",
        time_commitment="",
        schedule="",
        timezone="",
        virtual="",
        virtual_where="",
        action_type="",
    ):
        # get attribute/field arguments for params
        self.username = username
        self.password = password
        self.title = title
        self.event_kind = event_kind
        self.event_type = event_type
        self.description = description
        self.start_date = start_date
        self.start_hour = start_hour
        self.start_min = start_min
        self.start_ampm = start_ampm
        self.end_date = end_date
        self.end_hour = end_hour
        self.end_min = end_min
        self.end_ampm = end_ampm
        self.recurrence = recurrence
        self.time_commitment = time_commitment
        self.schedule = schedule
        self.timezone = timezone
        self.virtual = virtual
        self.virtual_where = virtual_where
        self.action_type = action_type

        self._start_session()
        self._publish()
        self._close_session()

class GivePulse(Website):
    def __init__(self):
        # GivePulse specific extra element locators and values: hard-coded, no worries of changing across time (presumebly)
        self.group_parent_group_locator = (By.ID, "Group_parent_group_id")
        self.group_submit_locator = (
            By.XPATH,
            "/html/body/div[1]/div[4]/div[2]/div/div[3]/div/div/div/div/div[2]/form/div[3]/div/div[2]/button",
        )
        self.unpublish_submit_locator = (
            By.XPATH,
            "/html/body/div[1]/div[4]/div[2]/div/div[4]/div[1]/div[2]/ul[5]/li[1]/a",
        )
        self.publish_submit_locator = (By.ID, "savePublish")

        # GivePulse concrete locator values
        super().__init__(
            URL="https://www.givepulse.com/login",
            login_username_locator=(By.NAME, "LoginForm[email]"),
            login_password_locator=(By.NAME, "LoginForm[password]"),
            login_submit_locator=(By.NAME, "yt0"),
            form_link_locator=(By.LINK_TEXT, "List Event"),
            post_title_locator=(By.NAME, "Event[title]"),
            post_evenkind_locator=(By.NAME, "Event[kind_of_event]"),
            post_eventtype_locator=(By.NAME, "Event[event_type]"),
            post_description_frame_locator=(By.ID, "Event_description_ifr"),
            post_description_locator=(By.ID, "tinymce"),
            post_event_start_date_select_locator=(By.ID, "Event_start_date_select"),
            post_event_start_hour_locator=(By.ID, "Event_start_hour"),
            post_event_start_min_locator=(By.ID, "Event_start_min"),
            post_event_start_ampm_locator=(By.ID, "Event_start_ampm"),
            post_event_end_date_select_locator=(By.ID, "Event_end_date_select"),
            post_event_end_hour_locator=(By.ID, "Event_end_hour"),
            post_event_end_min_locator=(By.ID, "Event_end_min"),
            post_event_end_ampm_locator=(By.ID, "Event_end_ampm"),
            form_submit_locator=(By.NAME, "yt0"),
        )

    def _login(self):
        # action on browser
        self.driver.get(self.website)
        # remaining steps are inherited from the parent website
        super()._login()

    def _enter_form(self):
        # some steps are inherited from the parent class
        super()._enter_form()
        # post descrpition #
        self.driver.switch_to.frame(
            self.driver.find_element(
                self.post_description_frame_locator[0],
                self.post_description_frame_locator[1],
            )
        )
        self.driver.find_element(
            self.post_description_locator[0], self.post_description_locator[1]
        ).send_keys(self.description)
        self.driver.switch_to.default_content()

        # type #
        Select(
            self.driver.find_element(
                self.post_evenkind_locator[0], self.post_evenkind_locator[1]
            )
        ).select_by_value(self.event_kind)
        Select(
            self.driver.find_element(
                self.post_eventtype_locator[0], self.post_eventtype_locator[1]
            )
        ).select_by_value(self.event_type)

        # when #
        self.driver.find_element(
            self.post_event_start_date_select_locator[0],
            self.post_event_start_date_select_locator[1],
        ).clear()
        self.driver.find_element(
            self.post_event_start_date_select_locator[0],
            self.post_event_start_date_select_locator[1],
        ).send_keys(self.start_date)
        Select(
            self.driver.find_element(
                self.post_event_start_hour_locator[0],
                self.post_event_start_hour_locator[1],
            )
        ).select_by_value(self.start_hour)
        Select(
            self.driver.find_element(
                self.post_event_start_min_locator[0],
                self.post_event_start_min_locator[1],
            )
        ).select_by_value(self.start_min)
        Select(
            self.driver.find_element(
                self.post_event_start_ampm_locator[0],
                self.post_event_start_ampm_locator[1],
            )
        ).select_by_value(self.start_ampm)

        self.driver.find_element(
            self.post_event_end_date_select_locator[0],
            self.post_event_end_date_select_locator[1],
        ).clear()
        self.driver.find_element(
            self.post_event_end_date_select_locator[0],
            self.post_event_end_date_select_locator[1],
        ).send_keys(self.end_date)
        Select(
            self.driver.find_element(
                self.post_event_end_hour_locator[0], self.post_event_end_hour_locator[1]
            )
        ).select_by_value(self.end_hour)
        Select(
            self.driver.find_element(
                self.post_event_end_min_locator[0], self.post_event_end_min_locator[1]
            )
        ).select_by_value(self.end_min)
        Select(
            self.driver.find_element(
                self.post_event_end_ampm_locator[0], self.post_event_end_ampm_locator[1]
            )
        ).select_by_value(self.end_ampm)

    def _select_group(self):
        # select Asha Hope Amanaki group #
        Select(
            self.driver.find_element(
                self.group_parent_group_locator[0], self.group_parent_group_locator[1]
            )
        ).select_by_value("493396")
        self.driver.find_element(
            self.group_submit_locator[0], self.group_submit_locator[1]
        ).click()
        sleep(
            5
        )  # wait until group info can load successfully and the driver can see submit button.

    def _publish(self):

        super()._publish()
        self._select_group()
        self.driver.find_element(
            self.publish_submit_locator[0], self.publish_submit_locator[1]
        ).click()
        sleep(5)  # wait until the next page load successfully
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[4]/div[2]/div/div[4]/div[1]/div[2]/ul[2]/li[3]/a",
        ).click()

    def unpublish(self):
        self.driver.find_element(
            self.unpublish_submit_locator[0], self.unpublish_submit_locator[1]
        ).click()

class VolunteerMatch(Website):
    def __init__(self):
        # VolunteerMatch specific extra element locators and values: hard-coded, no worries of changing across time (presumebly)
        self.login_link_locator = (By.ID, "global_login_link")
        self.contact_locator = (By.ID, "contact")
        self.virtrual_locator = (By.ID, "virtual_only")
        self.startdate_script = '$("input#start_date").'
        self.enddate_script = '$("input#end_date").'
        self.estVolunteer_locator = (By.ID, "estVolunteers")
        self.notcovid_locator = (By.ID, "not_c19_response")
        self.cause_locator = (
            By.XPATH,
            "/html/body/div[3]/div[2]/main/div/div[3]/div[1]/div/div/form/div[15]/div/div[1]/div/div[3]/div[2]/ul/li/ul/li[6]/a/span",
        )

        # VolunteerMatch concrete locator values
        super().__init__(
            URL="https://www.volunteermatch.org/login",
            login_username_locator=(By.ID, "login_username"),
            login_password_locator=(By.ID, "login_password"),
            login_submit_locator=(By.NAME, "login_button"),
            form_link_locator=(
                By.XPATH,
                "/html/body/div[4]/div/div[2]/div[3]/div[2]/div[3]/div[2]/a",
            ),
            post_title_locator=(By.ID, "titleData.title"),
            post_description_frame_locator=(By.ID, "descriptionData.description_ifr"),
            post_description_locator=(By.ID, "tinymce"),
            form_submit_locator=(By.ID, "save_publish_button"),
        )

    def _login(self):
        self.driver.get(self.website)
        main_page = self.driver.current_window_handle
        self.driver.find_element(
            self.login_link_locator[0], self.login_link_locator[1]
        ).click()  # open a popup login window
        self.driver.switch_to.window(
            main_page
        )  # switch to the main page to find login elements
        sleep(5) # wait until the main page can load
        super()._login()

    def _enter_form(self):
        super()._enter_form()
        # descrpition #
        self.driver.switch_to.frame(
            self.driver.find_element(
                self.post_description_frame_locator[0],
                self.post_description_frame_locator[1],
            )
        )
        self.driver.find_element(
            self.post_description_locator[0], self.post_description_locator[1]
        ).send_keys(self.description)
        self.driver.switch_to.default_content()

        # contact: ashahopeamanaki@gmail.com #
        Select(
            self.driver.find_element(self.contact_locator[0], self.contact_locator[1])
        ).select_by_value("26884010")

        # virtural/remore #
        self.driver.find_element(self.virtrual_locator[0], self.virtrual_locator[1]).click()

        # when #
        self.driver.execute_script(f'$("input#start_date").val("{self.start_date}")')
        self.driver.execute_script(f'$("input#end_date").val("{self.end_date}")')

        # paticipants needed #
        self.driver.find_element(
            self.estVolunteer_locator[0], self.estVolunteer_locator[1]
        ).send_keys("1")

        # covid #
        self.driver.find_element(self.notcovid_locator[0], self.notcovid_locator[1]).click()

        # causes #
        self.driver.find_element(self.cause_locator[0], self.cause_locator[1]).click()

    def _publish(self):
        
        super()._publish()
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[4]/div[2]/main/div[1]/div/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/ul[2]/li[2]/a",
        ).click()
        current_page = self.driver.current_window_handle
        all_pages = self.driver.window_handles
        for i in all_pages:
            if i != current_page:
                self.driver.switch_to.window(i)
                # enlarge the post page
                self.driver.maximize_window()

class Idealist(Website):
    def __init__(self):
        # Idealist specific extra element locators and values: hard-coded, no worries of changing across time (presumebly)
        self.form_link_locator_next = (
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div[2]/div/span/div/div/div[3]/div[2]/div[2]/div[5]/div/div[2]/div/div/div/div/a[2]",
        )
        self.volunteer_event_locator = (
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/button[3]",
        )
        self.applicant_tracker_locator = (
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[1]/div/div[2]/button[1]",
        )
        self.action_type_locator = (By.ID, "create-volop-form-action-type")
        self.next_page_locator = (
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[9]/div/button/div/div[1]",
        )
        self.one_time_locator = (By.XPATH, '//*[@id="create-volop-form-is-recurring"]')
        self.long_term_locator = (
            By.XPATH,
            '//*[@id="create-volop-form-is-recurring-true"]',
        )
        self.hours_locator = (By.ID, "create-volop-form-expected-time-FEW_HOURS")
        self.minutes_loctor = (By.ID, "create-volop-form-expected-time")
        self.days_locator = (By.ID, "create-volop-form-expected-time-FEW_DAYS")
        self.hours_week_locator = (By.ID, "create-volop-form-expected-time")
        self.hours_month_loctor = (
            By.ID,
            "create-volop-form-expected-time-FEW_HOURS_MONTH",
        )
        self.parttime_locator = (By.ID, "create-volop-form-expected-time-PART_TIME")
        self.fulltime_locator = (By.ID, "create-volop-form-expected-time-FULL_TIME")
        self.weekday_schedule_locator = (By.ID, "create-volop-form-times-of-day")
        self.weekend_schedule_locator = (
            By.ID,
            "create-volop-form-times-of-day-WEEKENDS",
        )
        self.add_date_locator = (
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div/div/div[2]/div/div/div/div/div[4]/div/div/button",
        )
        self.next_page_locator_2 = (
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/button/div/div[1]",
        )
        self.remote_locator = (
            By.ID,
            "create-volop-form-remote-options-location-type-REMOTE",
        )
        self.remote_where_locator = (
            By.ID,
            "create-volop-form-remote-options-remote-zone",
        )
        self.listing_address_locator = (
            By.ID,
            "create-volop-form-remote-options-use-org-address",
        )
        self.next_page_locator_3 = (
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/button/div/div[1]",
        )
        self.compliance_locator = (By.ID, "create-volop-form-in-accordance")

        # Idealist concrete locator values
        super().__init__(
            URL="https://www.idealist.org/login",
            login_username_locator=(By.ID, "login-form-email"),
            login_password_locator=(By.ID, "login-form-password"),
            login_submit_locator=(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div[5]/div/div/form/div/div[4]/button/div/div[1]",
            ),
            form_link_locator=(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div[2]/div/span/div/div/div[3]/div[2]/div[2]/div[5]/div/div[2]/div/a/div[1]",
            ),
            post_description_locator=(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[7]/div/div/div[2]/div/div/div/div/div[2]/div[1]",
            ),
            post_title_locator=(By.ID, "create-volop-form-name"),
            post_event_start_date_select_locator=(
                By.ID,
                "create-volop-form-start-date",
            ),
            post_event_end_date_select_locator=(By.ID, "create-volop-form-end-date"),
            form_submit_locator=(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[7]/div[2]/button/div/div[1]",
            ),
        )

    def _login(self):
        self.driver.get(self.website)
        super()._login()

    def _open_form(self):
        super()._open_form()
        self.driver.find_element(
            self.form_link_locator_next[0], self.form_link_locator_next[1]
        ).click()
        sleep(5)  # wait until the next page can load successfully
        self.driver.find_element(
            self.volunteer_event_locator[0], self.volunteer_event_locator[1]
        ).click()
        sleep(5)  # wait until the next page can load successfully
        self.driver.find_element(
            self.applicant_tracker_locator[0], self.applicant_tracker_locator[1]
        ).click()
        sleep(5)  # wait until the next page can load successfully

    def _enter_form(self):
        super()._enter_form()
        Select(
            self.driverr.find_element(
                self.action_type_locator[0], self.action_type_locator[1]
            )
        ).select_by_value(self.action_type)
        self.driver.find_element(
            self.post_description_locator[0], self.post_description_locator[1]
        ).send_keys(self.description)
        self.driver.find_element(
            self.next_page_locator[0], self.next_page_locator[1]
        ).click()
        sleep(2)  # wait until the next page can load successfully

        # recurrence and time commmitment #
        if self.recurrence == Recurrence.ONE_TIME.value:
            button = self.driver.find_element(
                self.one_time_locator[0], self.one_time_locator[1]
            )
            self.driver.execute_script(
                "arguments[0].click();", button
            )  # radio button clicks
            sleep(2)  # wait until time commitment options show
            if self.time_commitment == TimeCommitmentOneTime.FEW_HOURS.value:
                self.driver.find_element(
                    self.hours_locator[0], self.hours_locator[1]
                ).click()
            elif self.time_commitment == TimeCommitmentOneTime.FEW_MINUTES.value:
                self.driver.find_element(
                    self.minutes_loctor[0], self.minutes_loctor[1]
                ).click()
            elif self.time_commitment == TimeCommitmentOneTime.FEW_DAYS.value:
                self.driver.find_element(self.days_locator[0], self.days_locator[1]).click()
        elif self.recurrence == Recurrence.LONG_TERM.value:
            button = self.driver.find_element(
                self.long_term_locator[0], self.long_term_locator[1]
            )
            self.driver.execute_script("arguments[0].click();", button)
            sleep(2)  # wait until time commitment options show
            if self.time_commitment == TimeCommitmentLongTerm.FEW_HOURS_WEEK.value:
                self.driver.find_element(
                    self.hours_week_locator[0], self.hours_week_locator[1]
                ).click()
            elif self.time_commitment == TimeCommitmentLongTerm.FEW_HOURS_MONTH.value:
                self.driver.find_element(
                    self.hours_month_loctor[0], self.hours_month_loctor[1]
                ).click()
            elif self.time_commitment == TimeCommitmentLongTerm.PART_TIME.value:
                self.driver.find_element(
                    self.parttime_locator[0], self.parttime_locator[1]
                ).click()
            elif self.time_commitment == TimeCommitmentLongTerm.FULL_TIME.value:
                self.driver.find_element(
                    self.fulltime_locator[0], self.fulltime_locator[1]
                ).click()

        # schedule #
        if self.schedule == Schedule.WEEKDAYS:
            self.driver.find_element(
                self.weekday_schedule_locator[0], self.weekday_schedule_locator[1]
            ).click()
        elif self.schedule == Schedule.WEEKENDS:
            self.driver.find_element(
                self.weekend_schedule_locator[0], self.weekend_schedule_locator[1]
            ).click()
        sleep(5) # wait until the next page can load successfully

        # date #
        self.driver.find_element(self.add_date_locator[0], self.add_date_locator[1]).click()
        sleep(3)  # wait until date frame can load completely
        self.driver.find_element(
            self.post_event_start_date_select_locator[0],
            self.post_event_start_date_select_locator[1],
        ).send_keys(self.start_date)
        self.driver.find_element(
            self.post_event_end_date_select_locator[0],
            self.post_event_end_date_select_locator[1],
        ).send_keys(self.end_date)

        # next page #
        self.driver.find_element(
            self.next_page_locator_2[0], self.next_page_locator_2[1]
        ).click()
        sleep(2)  # wait until the next page can load sucessfully

        # virtual #
        if self.virtual:
            self.driver.find_element(self.remote_locator[0], self.remote_locator[1]).click()

        # where #
        Select(
            self.driver.find_element(
                self.remote_where_locator[0], self.remote_where_locator[1]
            )
        ).select_by_value(
            "COUNTRY"
        )  # whthin the U.S.

        # remote but listing related to waht address #
        self.driver.find_element(
            self.listing_address_locator[0], self.listing_address_locator[1]
        ).click()

        self.driver.find_element(
            self.next_page_locator_3[0], self.next_page_locator_3[1]
        ).click()
        sleep(2)  # wait until the next page can load sucessfully

        # compliance statement#
        self.driver.find_element(
            self.compliance_locator[0], self.compliance_locator[1]
        ).click()

    def _publish(self):
        super()._publish()
        sleep(5) # wait until next page can load successfully
        self.driver.find_element(By.XPATH, '//*[@id="idealist-modal-container"]').click()

class TimeCommitmentOneTime(Enum):
    FEW_HOURS = 0
    FEW_MINUTES = 1
    FEW_DAYS = 2

class TimeCommitmentLongTerm(Enum):
    FEW_HOURS_WEEK = 0
    FEW_HOURS_MONTH = 1
    PART_TIME = 2
    FULL_TIME = 3

class Recurrence(Enum):
    ONE_TIME = 0
    LONG_TERM = 1

class Schedule(Enum):
    WEEKDAYS = 0
    WEEKENDS = 1
