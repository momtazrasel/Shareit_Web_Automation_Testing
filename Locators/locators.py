from selenium.webdriver.common.by import By


class BusinessPageLocators(object):
    # Business Pages Locators
    click_business_xpath = (By.XPATH, "//*[@id='__layout']/div/header/ul/li[2]/div/span")
    click_overview_xpath = (By.XPATH, "/html/body/ul/li[1]/a")
    click_solution_xpath = (By.XPATH, "/html/body/ul/li[2]/a")
    click_success_stories_xpath = (By.XPATH, "/html/body/ul/li[3]/a")
    click_content_xpath = (By.XPATH, "/html/body/ul/li[4]/a")
    region_xpath = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/form/div[1]/div/div/div/input")
    select_region_xpath = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]")
    industry_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/form/div[2]/div/div/div[1]/input")
    industry_select = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span")
    objective_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/form/div[3]/div/div/div/input")
    objective_select_xpath = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span")
    first_name_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div/div[1]/input")
    last_name_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/input")
    select_country_code = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[3]/div/div/div/div/div"
                                     "/span/span/i")
    select_bd_code = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[184]")
    mobile_no_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[3]/div/div[1]/input")
    email_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[4]/div/div[1]/input")
    company_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[5]/div/div/input")
    job_title_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[6]/div/div/input")
    industry_select_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[7]/div/div/div/span"
                                       "/span/i")
    select_industry_xpath = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]")
    select_company_region = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[8]/div/div/div[1]/"
                                       "span/span/i")
    company_region_xpath = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]")
    message_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[9]/div/div/input")
    # check_box_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[10]/input")
    # checked_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/div[10]/div")
    submit_button_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[2]/div[2]/div[2]/form/button")


class ProductPageLocators(object):
    click_product_option = (By.XPATH, "//*[@id='__layout']/div/header/ul/li[3]/div/span")
    share_it_xpath = (By.XPATH, "/html/body/ul/li[1]")
    android_xpath = (By.XPATH, "//*[@id='__layout']/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]")
    clone_it_xpath = (By.XPATH, "/html/body/ul/li[2]/a")
    lock_it_xpath = (By.XPATH, "/html/body/ul/li[3]/a")
    lock_android = (By.XPATH, "/html/body/div[1]/div/div/div[2]/a/img")
    listen_it_xpath = (By.XPATH, "/html/body/ul/li[4]/a")
    clean_it_xpath = (By.XPATH, "/html/body/ul/li[5]/a")
    language_xpath = (By.XPATH, "//*[@id='__layout']/div/header/ul/li[7]/span[2]")


class NewsRoomLocators(object):
    newsroom_xpath = (By.XPATH, "/html/body/div/div/div/header/ul/li[4]/a")
    click_all_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div[1]")
    click_post_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[3]/div[1]/div[1]/img")
    click_twitter_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[3]/div[1]/img")
    click_facebook_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[3]/div[2]/img")
    see_more_xpath = "//*[@id='__layout']/div/div/div[2]/div[4]/a"
    company_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div[2]")
    industry_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div[3]")
    insight_xpath = (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div[4]")


class SRCLocators(object):
    src_xpath = (By.XPATH, "/html/body/div/div/div/header/ul/li[5]/div/span")
    overview_xpath = (By.XPATH, "/html/body/ul/li[1]")
    vulnerability_xpath = (By.XPATH, "/html/body/ul/li[2]/a")
    announcement_xpath = (By.XPATH, "/html/body/ul/li[3]/a")
