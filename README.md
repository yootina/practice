# 구조 생각해보기

1. 프로젝트 폴더 생성 > 프로젝트 생성
2. 가상환경 생성 > 가상환경 활성화
3. 가상환경에 django설치
4. 서버 실행 확인
5. 앱 생성 > 앱 등록 `settings.py`
6. `urls.py` > `views.py` > `templates/*.html`

## 공통적으로 사용하는 부분을 따로 html로 분리해서 사용해보기
- `settings.py`에 `TEMPLATE`에 설정값을 넣어주기
: 여기서 `TEMPLATE`은 `html`을 뜻하고 html에 대한 설정들을 해주는 옵션이고 현재까지는 articles폴더 안에 `templates`라는 폴더를 만들고 그 안에 `html`을 생성해왔다.
- django는 기본적으로 자동으로 templates라는 폴더가 있으면 자동으로 탐지를 하고 꺼내서 쓴다. (`APP_DIPS : True`)
- 기본적으로 모든 앱들을 탐지를 하는게 `True`옵션이고 `DIRS` 옵션은 기본적으로 앱 안에 있는 templates를 제외하고 그 외에 공간에 추가적으로 html를 탐지하기 위한 폴더를 등록하기 위한 공간.
- `BASE_DIR = Path(__file__).resolve().parent.parent` : `Path(__file__).resolve() : setting.py`를 말하고 `.parent.parent` 그 부모의 부모를 말하는것은 `settings.py`의 `parent`는 그 프로젝트 폴더의 `parent`는 최상단 폴더를 가리킨다.
- 최상단폴더에 `templates`라는 폴더를 생성하고 `base.html`을 생성한다.
- {% block body %} {% endblock %}를 넣는건 비워놓는 공간을 만들어놓는것.
