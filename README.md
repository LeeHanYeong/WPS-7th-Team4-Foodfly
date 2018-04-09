# FoodFly

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

- email
- password1
- password2

**Result**

```json
{
    "user": {
        "pk": 2,
        "email": "dev2@lhy.kr",
        "img_profile": null
    },
    "token": "b78a4e8a7b5e9053559468b341e0b7f6108ec419"
}
```


### 유저 인증 및 토큰정보 얻기

**URL**

`/members/auth-token/`

**Method**

`POST`

**Params**

- email
- password

**Result**

```json
{
    "user": {
        "pk": 1,
        "email": "dev@lhy.kr",
        "img_profile": null
    },
    "token": "235e29ae4ae294b54f369a3828190855517db1c7"
}
```

### 프로필 정보

> **인증필요**  
> 토큰값이 `235e29ae`인 경우,   
> HTTP Header의 `Authorization`키에 `Token 235e29ae`라는 값을 담아 요청해야 합니다.

**URL**

`/members/profile/`

**Method**

`POST`

**Result**

```json
{
    "pk": 1,
    "email": "dev@lhy.kr",
    "img_profile": null
}
```