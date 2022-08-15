 Task 1 Software configuration

    Subtask 1 Why did I choose to participate in the challenge portfolio?
        Hi, my name is Stanislav and this January I've started my transition to become a QA engineer. Since then I was participating in different QA schools that was mostly focused on manual testing. I always thought that many tasks (i.e. regression testing) should be done automatically. Last week I've started my first real, although non-comercial project, and now I'm totally convinced that I need to automize as many tasks as I could since my team is pretty big, my experience is pretty poor and commits..COMMITS.. ahh idk what to say.. let's just say that I will be very glad if I could make a big work once and then tweak it just a little later from time to time. 

        I want to study automatization with Python since I didn't really liked JS automatization (I've tried just a little mocha and chai). I'm still researching the right approach to automize my tasks as QA so I was really thrilled after applying to this Challenge and when I saw confirmation letter from you, so thank You!

        If everything will be good I would like to participate in some internship, although my primary goal is studying.
    
    Subtask 3 Commit
        My commit is named Pycharm setup

Task 2 Selectors
    Subtask 1 Searching for selectors on the login pageList all the elements that are on the login page.
    <!-- As I can see most locators will work only in certain conditions (such as chosen language or current state) so it's really tricky to find the most universal one that will be both compact and not dependable on it's location/language/etc. Most locators will be written for English version of the page -->
        Login_input_xpath
            #login
            //*[text()='Login']
            //*[@id='login']
            //input[@type='text']
            /html/body/div/form/div/div[1]/div[1]/div/input
        Password_input_xpath
            #password
            //*[text()='Password']
            //*[@id='password']
            //input[@type='password']
            /html/body/div/form/div/div[1]/div[2]/div/input
        Remind_password_hyperlink_xpath
            <!-- From Notion example
            //*[@id="__next"]/form/div/div[1]/a
            //*[text()="Remind password"]
            //child::div/a -->
            #__next > form > div > div.MuiCardContent-root > a
            /html/body/div/form/div/div[1]/a
        Language_dropdown_xpath
            #__next > form > div > div.MuiCardActions-root > div > div
            //*[@id="__next"]/form/div/div[2]/div/div
            /html/body/div/form/div/div[2]/div/div
            <!-- //*[@tabindex='-1"] there's also one more element using this exact tabindex, I'm pretty sure I can choose somehow exact one but I need some time to research, let's move on for now-->
                For English
                    //*[@value='en']
                    //*[@id="menu-"]/div[3]/ul/li[2]
                    /html/body/div[2]/div[3]/ul/li[2]
                For Polski
                    //*[@value='pl']
                    //*[@id="menu-"]/div[3]/ul/li[1]
                    /html/body/div[2]/div[3]/ul/li[1]
        Sign-in_button_xpath
            #__next > form > div > div.MuiCardActions-root > button
            //*[@id="__next"]/form/div/div[2]/button
            /html/body/div/form/div/div[2]/button
            //*[@type='submit']
            //span[text()='Sign in']
            //*[text()='Sign in']

        