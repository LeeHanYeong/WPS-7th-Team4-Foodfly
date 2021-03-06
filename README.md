# FoodFly

## 변경사항

- 18.04.11
	- 요청 / 응답의 키가 자바스크립트 명명 규칙을 따라 `lower_case_with_underscores(Snake Case)`에서 `CapitalizeWords by initial lowercase(Camel Case)`로 변경됩니다.
		- `phone_number` -> `phoneNumber`
		- `img_profile` -> `imgProfile`
	- 음식점 목록, 음식점 상세 API추가

## 기본정보

**Base URL**  
`https://foodfly.lhy.kr`

**관리자 사이트**  
`https://foodfly.lhy.kr/admin/`


## 회원 관련

### 회원 가입

**URL**

`/members/signup/`

**Method**

`POST`

**Params**

- **name**
- **phoneNumber**
	- 국가번호가 필요합니다. ex) +82 010-0000-0000
	- [국제전화 나라 번호](https://ko.wikipedia.org/wiki/%EA%B5%AD%EC%A0%9C%EC%A0%84%ED%99%94_%EB%82%98%EB%9D%BC_%EB%B2%88%ED%98%B8)를 참조하세요
	- 돌려주는 데이터에서는 국가번호가 빠져있습니다.
- **email**
- **password1**
- **password2**

**Result**

```json
{
    "user": {
        "pk": 2,
        "name": "이한영",
        "phoneNumber": "010-1234-1234",
        "email": "dev2@lhy.kr",
        "imgProfile": null
    },
    "token": "c7c6ddd46faad6f1676458d2e8c8eadc42c3da00"
}
```


### 유저 인증 및 토큰정보 얻기

**URL**

`/members/auth-token/`

**Method**

`POST`

**Params**

- **email**
- **password**

**Result**

```json
{
    "user": {
        "pk": 2,
        "name": "이한영",
        "phoneNumber": "010-1234-1234",
        "email": "dev2@lhy.kr",
        "imgProfile": null
    },
    "token": "c7c6ddd46faad6f1676458d2e8c8eadc42c3da00"
}
```

### 프로필 정보

> **인증필요**  
> 토큰값이 `235e29ae`인 경우,   
> HTTP Header의 `Authorization`키에 `Token 235e29ae`라는 값을 담아 요청해야 합니다.

**URL**

`/members/profile/`

**Method**

`GET`

**Result**

```json
{
    "pk": 2,
    "name": "이한영",
    "phoneNumber": "010-1234-1234",
    "email": "dev2@lhy.kr",
    "imgProfile": null
}
```


## 음식점 및 메뉴 관련

## 음식점 리스트

**URL**

`/restaurants/`

**Method**

`GET`

**Result**

구조

```json
[
	{
		"음식점 정보들",
		"음식점 정보들",
		"음식점 정보들",
		"categories": [음식점의 카테고리 목록],
		"tags": [음식점의 분류 목록],
		"orderTypes": [음식점의 주문유형 목록]
	}
]
```

실제 데이터

```json
[
    {
        "pk": 1,
        "name": "셰플리 강남키친",
        "address": "서울 강남구 역삼동 724-46 1층 키친",
        "minOrderPrice": 9900,
        "avgDeliveryTime": "00:40",
        "restaurantInfo": "[CHEFLY] 당신만을 위한 셰프의 한끼\r\n\r\n\r\n\r\n대한민국 대표 셰프들의 요리를 \r\n\r\n온라인주문+즉시조리+즉시배송으로 \r\n\r\n원하는 시간과 장소에서 편하게 즐기실 수 있는 \r\n\r\n신개념 온라인 음식배달 서비스입니다",
        "originInfo": "[메인메뉴_완조리]\r\n\r\n\r\n\r\n데미그라스 소스를 얹은 경양식 함박스테이크 : 돼지고기(국내산), 소고기(호주산), 채소류(국내산), 미니당근(미국산), 스파게티니(이탈리아산)\r\n\r\n차돌박이 야키소바 : 차돌박이(미국산), 가쓰오부스(일본산), 채소류(국내산), 숙주(중국산), 초생강(중국산)\r\n\r\n그라나파다노를 곁들인 닭다리살 김치볶음밥 : 김치(국내산), 쌀(국내산), 계란(국내산), 채소류(국내산), 정육(브라질산), 그라나파다노(이탈리아산), 트러플오일(이탈리아산), 굴소스(홍콩산), 두반장(중국산)\r\n\r\n소불고기 궁중 비빔밥 '골동반' : 소고기(호주산), 계란(국내산), 시금치(국내산), 튀각(국내산), 쌀(국내산), 미역(국내산), 고사리(중국산), 당근(중국산), 청포묵(중국산), 숙주(중국산), 은행(중국산)\r\n\r\n국내산 생등심 돈가츠 덮밥 '가츠동' : 돼지등심(국내산) 계란(국내산) 쌀(국내산) 채소류(국내산) 간장(일본산) 단무지(중국산) 락교(중국산)\r\n\r\n데리야끼 치킨 라이스 : 닭고기(브라질산) 채소류(국내산) 쌀(국내산)\r\n터머릭 치킨 & 아보카도 샌드위치 : 닭고기(브라질산) 아보카도(미국산) 터머릭파우더(인도산) 감자(국내산) 채소류(국내산) 홀그레인머스터드(미국산)\r\n아보카도를 곁들인 연어회덮밥 : 연어(노르웨이산)  아보카도(미국산) 채소류(국내산) 쌀(국내산) 계란(국내산) 날치알(인도네시아산)\r\n봄나물무침을 곁들인 대패삼겹살 덮밥과 바지락 된장찌개 : 삼겹살(네덜란드) 쌀(국내산) 채소류(국내산) 고추가루(국내산)\r\n허니갈릭 닭가슴살 스테이크를 얹은 시저샐러드 : 로메인(국내산) 닭가슴살(국내산) 계란(국내산) 베이컨(수입산) 디종머스터드(미국산)\r\n\r\n[사이드메뉴_완조리]\r\n명란마요소스 치킨 가라아게 (5조각) : 정육(태국산), 명란(러시아산)\r\n지중해식 문어 샐러드 : 문어(중국산) 채소류(국내산) 썬드라이토마토(미국산) 그린올리브(이태리산) 블랙올리브(스페인산) 트러플오일(이태리산)\r\n트러플향 감자튀김 : 감자튀김(미국산) 트러플오일(이탈리아산)\r\n새우&양배추 웜샐러드, 감베리 까볼로 소테 : 채소류(국내산) 새우(베트남산)\r\n뉴욕식 버팔로윙 (5조각) : 치킨윙(태국산)\r\n미니 양배추와 그린 빈스 샐러드 : 미니양배추(중국산) 그린빈(호주산)\r\n쉬림프 카포나타와 갈릭브레드 : 새우(베트남산)",
        "categories": [
            {
                "pk": 1,
                "name": "한식"
            }
        ],
        "tags": [
            {
                "pk": 1,
                "name": "도시락"
            },
            {
                "pk": 2,
                "name": "샐러드"
            },
            {
                "pk": 3,
                "name": "한식"
            },
            {
                "pk": 4,
                "name": "치킨"
            },
            {
                "pk": 5,
                "name": "샌드위치"
            },
            {
                "pk": 6,
                "name": "단체주문"
            },
            {
                "pk": 7,
                "name": "단체배달"
            },
            {
                "pk": 8,
                "name": "일식"
            },
            {
                "pk": 9,
                "name": "비빔밥"
            }
        ],
        "orderTypes": [
            {
                "pk": 1,
                "name": "푸드플라이 배달"
            }
        ]
    }
]
```


## 음식점 상세

리스트와 비슷하나 배열 대신 하나의 `Restaurant`객체를 반환하며, 추가적으로 메뉴정보를 `menuCategories`항목에 가지고 있습니다.

**URL**

`/restaurants/<pk>/`

**Method**

`GET`

**Result**

구조

```json
{
	"음식점 정보들",
	"음식점 정보들",
	"음식점 정보들",
	"categories": [음식점의 카테고리 목록],
	"tags": [음식점의 분류 목록],
	"orderTypes": [음식점의 주문유형 목록],
	"menuCategoreis": [
		{
			"카테고리 정보들",
			"menus": [메뉴 정보 목록]
		}
	]
}
```

실제 데이터

```json
{
    "pk": 1,
    "name": "셰플리 강남키친",
    "address": "서울 강남구 역삼동 724-46 1층 키친",
    "minOrderPrice": 9900,
    "avgDeliveryTime": "00:40",
    "restaurantInfo": "[CHEFLY] 당신만을 위한 셰프의 한끼\r\n\r\n\r\n\r\n대한민국 대표 셰프들의 요리를 \r\n\r\n온라인주문+즉시조리+즉시배송으로 \r\n\r\n원하는 시간과 장소에서 편하게 즐기실 수 있는 \r\n\r\n신개념 온라인 음식배달 서비스입니다",
    "originInfo": "[메인메뉴_완조리]\r\n\r\n\r\n\r\n데미그라스 소스를 얹은 경양식 함박스테이크 : 돼지고기(국내산), 소고기(호주산), 채소류(국내산), 미니당근(미국산), 스파게티니(이탈리아산)\r\n\r\n차돌박이 야키소바 : 차돌박이(미국산), 가쓰오부스(일본산), 채소류(국내산), 숙주(중국산), 초생강(중국산)\r\n\r\n그라나파다노를 곁들인 닭다리살 김치볶음밥 : 김치(국내산), 쌀(국내산), 계란(국내산), 채소류(국내산), 정육(브라질산), 그라나파다노(이탈리아산), 트러플오일(이탈리아산), 굴소스(홍콩산), 두반장(중국산)\r\n\r\n소불고기 궁중 비빔밥 '골동반' : 소고기(호주산), 계란(국내산), 시금치(국내산), 튀각(국내산), 쌀(국내산), 미역(국내산), 고사리(중국산), 당근(중국산), 청포묵(중국산), 숙주(중국산), 은행(중국산)\r\n\r\n국내산 생등심 돈가츠 덮밥 '가츠동' : 돼지등심(국내산) 계란(국내산) 쌀(국내산) 채소류(국내산) 간장(일본산) 단무지(중국산) 락교(중국산)\r\n\r\n데리야끼 치킨 라이스 : 닭고기(브라질산) 채소류(국내산) 쌀(국내산)\r\n터머릭 치킨 & 아보카도 샌드위치 : 닭고기(브라질산) 아보카도(미국산) 터머릭파우더(인도산) 감자(국내산) 채소류(국내산) 홀그레인머스터드(미국산)\r\n아보카도를 곁들인 연어회덮밥 : 연어(노르웨이산)  아보카도(미국산) 채소류(국내산) 쌀(국내산) 계란(국내산) 날치알(인도네시아산)\r\n봄나물무침을 곁들인 대패삼겹살 덮밥과 바지락 된장찌개 : 삼겹살(네덜란드) 쌀(국내산) 채소류(국내산) 고추가루(국내산)\r\n허니갈릭 닭가슴살 스테이크를 얹은 시저샐러드 : 로메인(국내산) 닭가슴살(국내산) 계란(국내산) 베이컨(수입산) 디종머스터드(미국산)\r\n\r\n[사이드메뉴_완조리]\r\n명란마요소스 치킨 가라아게 (5조각) : 정육(태국산), 명란(러시아산)\r\n지중해식 문어 샐러드 : 문어(중국산) 채소류(국내산) 썬드라이토마토(미국산) 그린올리브(이태리산) 블랙올리브(스페인산) 트러플오일(이태리산)\r\n트러플향 감자튀김 : 감자튀김(미국산) 트러플오일(이탈리아산)\r\n새우&양배추 웜샐러드, 감베리 까볼로 소테 : 채소류(국내산) 새우(베트남산)\r\n뉴욕식 버팔로윙 (5조각) : 치킨윙(태국산)\r\n미니 양배추와 그린 빈스 샐러드 : 미니양배추(중국산) 그린빈(호주산)\r\n쉬림프 카포나타와 갈릭브레드 : 새우(베트남산)",
    "categories": [
        {
            "pk": 1,
            "name": "한식"
        }
    ],
    "tags": [
        {
            "pk": 1,
            "name": "도시락"
        },
        {
            "pk": 2,
            "name": "샐러드"
        },
        {
            "pk": 3,
            "name": "한식"
        },
        {
            "pk": 4,
            "name": "치킨"
        },
        {
            "pk": 5,
            "name": "샌드위치"
        },
        {
            "pk": 6,
            "name": "단체주문"
        },
        {
            "pk": 7,
            "name": "단체배달"
        },
        {
            "pk": 8,
            "name": "일식"
        },
        {
            "pk": 9,
            "name": "비빔밥"
        }
    ],
    "orderTypes": [
        {
            "pk": 1,
            "name": "푸드플라이 배달"
        }
    ],
    "menuCategories": [
        {
            "pk": 1,
            "restaurant": 1,
            "name": "사이드",
            "menus": [
                {
                    "category": 1,
                    "name": "명란 마요소스 치킨 가라아게 (5조각)",
                    "info": "겉은 바삭하고 속은 촉촉하게 튀겨낸 닭다리살을 명란과 마요네즈 등으로 셰프가 직접 배합하여 만든 특제 소스에 찍어먹는 일본 대표 가정식 \r\n*원산지 :정육(태국산), 명란(러시아산)",
                    "img": "http://foodfly.lhy.kr/media/menu/8660196975a41134572913.jpg",
                    "price": 5000
                },
                {
                    "category": 1,
                    "name": "지중해식 문어 샐러드",
                    "info": "수비드하여 부드러운 문어와 감자, 올리브, 루꼴라 등 신선한 재료들을 직접 만든 특제소스와 트러플오일로 버무려낸 셰플리 시그니처 샐러드\r\n*원산지 : 문어(중국산), 채소류(국내산), 썬드라이토마토(미국산), 그린올리브(이태리산), 블랙올리브(스페인산), 트러플오일(이태리산)",
                    "img": "http://foodfly.lhy.kr/media/menu/174118969059b15293a573b.jpg",
                    "price": 5500
                }
            ]
        }
    ]
}
```