// store user info and status

import {defineStore} from "pinia";
import {isLoginedUser} from "@/utils/token.js";

export const useUserStore = defineStore('userStore', {
    state() {
        return {
            userInfo: {},
            isLogin: isLoginedUser()
        }
    },
    actions: {
        setIsLogin(data) {
            this.isLogin = data;
        },
        setUserInfo(data) {
            this.userInfo = data;
        },
        addToken(data) {
            this.userInfo.tokens.push(data);
        },
        deleteToken(token_name) {
            let index = this.userInfo.tokens.findIndex(item => item.name === token_name);
            this.userInfo.tokens.splice(index, 1);
        }
    }
})

export const useUsersStore = defineStore('usersStore', {
    state() {
        return {
            users: [],
        }
    },
    actions: {
        setUsers(data) {
            this.users = data;
        }
    }
})