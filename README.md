# FoodFly

## 변경사항

- 18.04.11
	- 요청 / 응답의 키가 자바스크립트 명명 규칙을 따라 `lower_case_with_underscores(Snake Case)`에서 `CapitalizeWords by initial lowercase(Camel Case)`로 변경됩니다.
		- `phone_number` -> `phoneNumber`
		- `img_profile` -> `imgProfile`

## 기본정보

**Base URL**  
`https://foodfly.lhy.kr`


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