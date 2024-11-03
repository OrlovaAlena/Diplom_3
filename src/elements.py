from selenium.webdriver.common.by import By


class Elements:
    # восстановление пароля
    RESTORE_PASSWORD_BUTTON = By.CSS_SELECTOR, "a[href = '/forgot-password'"
    RESTORE_PASSWORD_SIGN = By.XPATH, ".//h2[text()='Восстановление пароля']"

    RESTORE_BUTTON = By.XPATH, ".//form/button[text() = 'Восстановить']"
    CONFIRM_BUTTON = By.XPATH, ".//form/button[text() = 'Сохранить']"

    #  сброс пароля
    EYE_ICON = By.XPATH, ".//div[contains(@class,  'input__icon')]"
    PASSWORD_INPUT_RESET = By.NAME, 'Введите новый пароль'

    # логин
    SIGN_IN_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    PASSWORD_INPUT = By.NAME, 'Пароль'
    CONFIRM_LOGIN_BUTTON = By.XPATH, ".//form/button[text() = 'Войти']"
    EMAIL_INPUT = By.XPATH, ".//div[label[text()='Email']]/input"

    # личный кабинет
    PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"
    ORDER_HISTORY = By.XPATH, ".//a[text()='История заказов']"
    EXIT = By.XPATH, ".//button[text()='Выход']"

    # history
    FIRST_ORDER_NUM = By.XPATH, ".//div/ul/li[1]//p"

    # header
    CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"
    ORDER_LIST = By.XPATH, ".//p[text()='Лента Заказов']"

    # ingredient
    FLUORESCENT_BUN = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a"
    COUNTER_FLOUR_BUN = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/..//p[1]"

    # main
    ORDER = By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"
    CREATE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    LOADING_ANIMATION = By.XPATH, ".//img[@alt = 'loading animation']"

    # modals main
    MODAL = By.XPATH, ".//h2[text() = 'Детали ингредиента']/../../.."
    MODAL_TITLE = By.XPATH, ".//h2[text() = 'Детали ингредиента']"
    MODAL_CLOSE_BUTTON = By.XPATH, ".//section[contains(@class, 'opened')]//button"
    ORDER_CREATED_SIGN = By.XPATH, ".//p[text()='Ваш заказ начали готовить']"
    ORDER_NUMBER = By.XPATH, ".//h2[contains(@class, 'Modal_modal')]"
    ORDER_NUMBER_DEFAULT = By.XPATH, ".//h2[text()='9999']"

    # feed
    ORDER_HEADER_SIGN = By.XPATH, ".//h1[text()='Лента заказов']"
    ORDER_CARD = ".//p[contains(text(), '"
    END = "')]"

    ALL_TIME_COUNTER = By.XPATH, ".//p[text()='Выполнено за все время:']/parent::div/p[2]"
    DAY_COUNTER = By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::div/p[2]"

    ORDERS_IN_PROGRESS = By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li"
    ALREADY_DONE = By.XPATH, ".//li[text()='Все текущие заказы готовы!']"

    # modals order
    MODAL_ORDER_DETAILS = By.XPATH, ".//div[contains(@class, 'Modal_order')]"
    MODAL_ORDER_NUMBER = By.XPATH, ".//div[contains(@class, 'Modal_order')]/p"
