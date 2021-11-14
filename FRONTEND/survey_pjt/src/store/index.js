import Vue from "vue";
import Vuex from "vuex";

import createPersistedState from "vuex-persistedstate";
import cookies from "vue-cookies";
import axios from "axios";

import router from "@/router";
import SERVER from "@/api/drf";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths: ["originFormData", "Students", "savedData"],
    }),
  ],
  state: {
    signupErr: {
      overlabErr: false,
      usernameErr: false,
      password1Err: false,
      password2Err: false,
      shortErr: false,
      diffErr: false,
      commonErr: false,
      emailErr: false,
      emailValidErr: false,
      emailOverlabErr: false,
    },
    loginErr: {
      usernameErr: false,
      emailErr: false,
      passwordErr: false,
    },
    // student
    Students: [],

    // auth
    authToken: cookies.get('auth-token'),
    surveys: [],
    responses: [],
    savedData: {
      answers: [],
      questions: [], 
      survey: {
        pk: null,
        title: 'title',
        description: 'description',
        color: '#FFCDD2',
        user: {
          pk: null,
          username: null,
          email: null
        }
      },
    },
    resetForm: {
      answers: [],
      questions: [], 
      survey: {
        pk: null,
        title: "title",
        description: "description",
        color: null,
        user: {
          pk: null,
          username: null,
          email: null,
        }
      },
    },
    originFormData: {
      answers: [],
      questions: [], 
      survey: {
        pk: null,
        title: 'title',
        description: 'description',
        color: '#FFCDD2',
        user: {
          pk: null,
          username: null,
          email: null
        }
      },
    },
    tmpData: {},
    studentData: {},
    isSaved: false,
    answerData: null,
  },
  getters: {
    //student
    studentsCount: (state) => state.Students.length,
    // auth
    isLoggedIn: (state) => !!state.authToken,
    // auth, etc
    config: (state) => ({ headers: { Authorization: `Token ${state.authToken}` } }),
  },
  mutations: {
    //addStudent
    addStudent: (state, dataList) => {
      dataList[0].flag = true;
      dataList[0].pk = dataList[1]
      state.Students.push(dataList[0]);
    },
    addStudents: (state, payload) => {
      payload.forEach(function (e) {
        const findItem = state.Students.find(function (item) {
          return item.s_num === e.s_num;
        });
        if(!findItem) {
          e.flag = true
          state.Students.push(e)
        }
      })
    },
    SET_SURVEYRES(state, resData) {
      state.answerData = resData
    },
    SET_STUDENT(state, studentData) {
      state.studentData = studentData
    },
    SET_RES(state, res) {
      state.tmpData = res
    },
    SET_IDERROR(state) {
      state.loginErr.usernameErr = true
      state.loginErr.emailErr = false
      state.loginErr.passwordErr = false
    },
    SET_EMAILERROR(state) {
      state.loginErr.usernameErr = false
      state.loginErr.emailErr = true
      state.loginErr.passwordErr = false
    },
    SET_PASSWORDERROR(state) {
      state.loginErr.usernameErr = false
      state.loginErr.emailErr = false
      state.loginErr.passwordErr = true
    },
    SET_LOGINERROR(state) {
      state.loginErr.usernameErr = true
      state.loginErr.emailErr = true
      state.loginErr.passwordErr = true
    },
    SET_OVERLABERR(state) {
      state.signupErr.overlabErr = true
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_NULLERR(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = true
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_PASSWORD1(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = true
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_SHORTERR(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = true
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_COMMONERR(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = true
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_DIFFERR(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = true
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_PASSWORD2(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = true
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_EMAILERR(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = true
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = false
    },
    SET_EMAILVALIDERR(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = true
      state.signupErr.emailOverlabErr = false
    },
    SET_EMAILOVERLABERR(state) {
      state.signupErr.overlabErr = false
      state.signupErr.usernameErr = false
      state.signupErr.password1Err = false
      state.signupErr.password2Err = false
      state.signupErr.shortErr = false
      state.signupErr.diffErr = false
      state.signupErr.commonErr = false
      state.signupErr.emailErr = false
      state.signupErr.emailValidErr = false
      state.signupErr.emailOverlabErr = true
    },
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_QUESTIONS(state, questions) {
      state.surveys = questions
      state.originFormData = {
        answers: [],
        questions: [], 
        survey: {
          pk: null,
          title: 'title',
          description: 'description',
          color: '#FFCDD2',
          user: {
            pk: null,
            username: null,
            email: null
          }
        },
      }
    },
    SET_EDITFORM(state, questionData) {
      state.originFormData = questionData
    },
    SET_RESPONSE(state, resultData) {
      state.responses = resultData
    },
    SET_ORIGINFORM(state, pk) {
      state.originFormData.survey.pk = pk
    },
    SET_SURVEYTOQUESTION(state, pk) {
      state.originFormData.questions[0].surveyss.push(pk)
    },
    SET_QUESTIONFORM(state, pk) {
      var end = state.originFormData.questions.length - 1
      state.originFormData.questions[end].pk = pk
    },
    SET_OPTIONFORM(state, pk) {
      var end = state.originFormData.answers.length - 1
      state.originFormData.answers[end].pk = pk
    },
    saveAlert(state) {
      state.isSaved = true;
      setTimeout(() => (state.isSaved = false), 3000);
    },
  },
  actions: {
    registerStudent: ({ commit }, payload) => {
      //학생등록하는곳으로 보내기
      axios.post(SERVER.URL + SERVER.ROUTES.registerStudent, payload)
      .then((res) => {
          commit("addStudent", [payload, res.data.st_pk]);
        })
        .catch((err) => console.log(err.response.data));
    },
    getStudents: ({ commit }) => {
      axios.post(SERVER.URL + SERVER.ROUTES.getStudent)
        .then((res) => {
          commit("addStudents", res.data);
        })
        .catch((err) => console.log(err.response.data));
    },
    //updateStudent
    updateStudent: ({ commit }, payload) => {
      commit
      axios.post(SERVER.URL + SERVER.ROUTES.updateStudent, payload)
        .then((res) => {
          console.log(res.data);

        })
        .catch((err) => console.log(err.response.data));
    },
    //deleteStudent
    deleteStudent: ({ commit }, pk) => {
      commit
      let info = { "pk": pk }
      axios.post(SERVER.URL + SERVER.ROUTES.deleteStudent, info)
        .then(() => {})
        .catch((err) => console.log(err.response.data));

    },
    // auth
    postAuthData({ commit }, info) {
      axios.post(SERVER.URL + info.location, info.data)
        .then((res) => {
          commit("SET_TOKEN", res.data.key);
          router.push({ name: "Main" });
        })
        .catch((err) => {
          if (info.location === '/api/rest-auth/login/') {
            if (!info.data.username) {
              commit("SET_IDERROR")
            } else if (!info.data.email) {
              commit("SET_EMAILERROR")
            } else if (!info.data.password){
              commit("SET_PASSWORDERROR")
            } else {
              commit("SET_LOGINERROR")
            }
          } else if (info.location === '/api/rest-auth/signup/') {
            if (err.response.data.username) {
              if (err.response.data.username[0] === "A user with that username already exists.") {
                commit("SET_OVERLABERR")
              } else if (err.response.data.username[0] === "This field may not be null." || err.response.data.username[0] === "This field may not be blank.") {
                commit("SET_NULLERR")
              }
            } else if (err.response.data.email) {
                if(err.response.data.email[0] === "This field may not be null.") {
                  commit("SET_EMAILERR")
                } else if (err.response.data.email[0] === "Enter a valid email address.") {
                  commit("SET_EMAILVALIDERR")
                } else if (err.response.data.email[0] === "A user is already registered with this e-mail address.") {
                  commit("SET_EMAILOVERLABERR")
                }
            } else if (err.response.data.password1) {
                if (err.response.data.password1[0] === "This field may not be null." || err.response.data.password1[0] === "This field may not be blank.") {
                  commit("SET_PASSWORD1")
                } else if (err.response.data.password1[0] === "This password is too short. It must contain at least 8 characters.") {
                  commit("SET_SHORTERR")
                } else if (err.response.data.password1[0] === "This password is too common.") {
                  commit("SET_COMMONERR")
                }
            } else if (!err.response.data.password1 && err.response.data.password2) {
                commit("SET_PASSWORD2")
            } else if (err.response.data.non_field_errors) {
                commit("SET_DIFFERR")
            }
          }
        });
    },
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.signup,
      };
      dispatch("postAuthData", info);
    },
    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.login,
      };
      dispatch("postAuthData", info);
    },
    logout({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => {
          // Django DB 에서는 삭제 | cookie, state 에는 남아있음
          commit("SET_TOKEN", null); // state 에서도 삭제
          cookies.remove("auth-token"); // cookie 에서는 삭제
        })
        .catch((err) => console.log(err.response));
    },
    fetchSurveys({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.surveyList, null, getters.config)
        .then((res) => commit("SET_QUESTIONS", res.data))
        .catch((err) => console.error(err));
    },
    fetchEditForm({ getters, commit }, survey) {
      axios.post(SERVER.URL + SERVER.ROUTES.getResponse, {'pk': survey.pk}, getters.config)
        .then((res) => {
          commit('SET_RESPONSE', res.data)
          axios.post(SERVER.URL + SERVER.ROUTES.surveyDetail, survey, getters.config)
            .then((res) => {
              commit('SET_EDITFORM', res.data)
              router.push({ name: 'EditSurvey' })
            })
            .catch(err => console.error(err))
        })
        .catch(err => console.error(err))
    },
    fetchResponseForm({ commit }, data) {
      axios.post(SERVER.URL + SERVER.ROUTES.surveyDetail, {'pk': data[1]})
        .then((res) => {
          commit('SET_RES', res.data)
          router.push({ name: 'Response', query: { name: data[0], s_pk: data[1], s_num: data[2] } })
        })
        .catch(err => console.error(err))
    },
    fetchStudent({ commit }, s_num) {
      axios.post(SERVER.URL + SERVER.ROUTES.getStudentInfo, {'s_num': s_num})
        .then((res) => {
          commit('SET_STUDENT', res.data)
        })
        .catch(err => console.error(err))
    },
    fetchStudentResponse({ commit }, s_pk) {
      axios.post(SERVER.URL + SERVER.ROUTES.getStudentResponse, {'s_pk': s_pk})
        .then((res) => {
          commit('SET_SURVEYRES', res.data)
        })
        .catch(err => console.error(err))
    },
    createSurvey({ getters, commit }, surveyData) {
      axios.post(SERVER.URL + SERVER.ROUTES.createSurvey, surveyData, getters.config)
        .then((res) => {
          commit('SET_ORIGINFORM', res.data.s_pk)
          router.push({ name: 'CreateSurvey' })
        })
        .catch(err => console.log(err.response.data))
    },
    editSurvey({ getters }, editData) {
      if (editData.answers) {
        editData.answers.forEach(answer => {
            axios.post(SERVER.URL + SERVER.ROUTES.updateOption, answer, getters.config)
              .then(() => {})
              .catch((err) => console.log(err.response.data));
        })
      }
      if (editData.questions) {
        editData.questions.forEach((question) => {
          if (question.pk !== null) {
            axios.post(SERVER.URL + SERVER.ROUTES.updateQuestion, question, getters.config)
              .then(() => {})
              .catch((err) => console.log(err.response.data));
            }
        })
      }
      axios.post(SERVER.URL + SERVER.ROUTES.updateSurvey, editData, getters.config)
        .then(() => {})
        .catch(err => console.log(err.response.data))
    },
    deleteSurvey({ getters }, surveyData) {
      if (surveyData.questions) {
        surveyData.questions.forEach(question => {
          axios.post(SERVER.URL + SERVER.ROUTES.deleteQuestion, question, getters.config)
            .then(() => {})
            .catch(err => console.log(err.response.data))
        });
      }
      axios.post(SERVER.URL + SERVER.ROUTES.deleteSurvey, surveyData.survey, getters.config)
        .then(() => {
          router.push({ name: 'SurveyList' })
        })
        .catch(err => console.log(err.response.data))
    },
    createQuestion({ getters, commit }, question) {
      axios.post(SERVER.URL + SERVER.ROUTES.createQuestion, question, getters.config)
        .then((res) => {
          commit("SET_QUESTIONFORM", res.data.q_pk);
        })
        .catch(err => console.log(err.response.data))
    },
    deleteQuestion({ getters }, question) {
      axios.post(SERVER.URL + SERVER.ROUTES.deleteQuestion, question, getters.config)
        .then(() => {})
        .catch(err => console.log(err.response.data))
    },
    createOption({ getters, commit }, info) {
      info[0].q_pk = info[1]
      axios.post(SERVER.URL + SERVER.ROUTES.createOption, info[0], getters.config)
        .then((res) => {
          commit("SET_OPTIONFORM", res.data.a_pk);
        })
        .catch(err => console.log(err.response.data))
    },
    deleteOption({ getters }, answer) {
      axios.post(SERVER.URL + SERVER.ROUTES.deleteOption, answer, getters.config)
        .then(() => {})
        .catch(err => console.log(err.response.data))
    },
    submitAnswer({ getters }, answerForm) {
      getters
      axios.post(SERVER.URL + SERVER.ROUTES.responseSurvey, answerForm)
        .then(() => {})
        .catch(err => console.log(err.response.data))
    },
    sendAlert({ getters }, sData) {
      axios.post(SERVER.URL + SERVER.ROUTES.sendAlert, sData, getters.config)
        .then(() => {})
        .catch(err => console.log(err.response.data))
    }
  },
  modules: {},
});
