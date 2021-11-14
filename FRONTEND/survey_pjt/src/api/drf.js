export default {
    // URL: 'http://i3b108.p.ssafy.io:8000',
    URL: 'http://localhost:8000',
    ROUTES: {
        deleteStudent: '/api/accounts/delete/student/',
        updateStudent: '/api/accounts/update/student/',
        getStudent: '/api/accounts/list/student/',
        getStudentInfo: '/api/accounts/get/student/',
        registerStudent: '/api/accounts/register/student/',
        signup: '/api/rest-auth/signup/',
        login: '/api/rest-auth/login/',
        logout: '/api/rest-auth/logout/',
        surveyList: '/api/surveys/list/',
        createSurvey: '/api/surveys/create/',
        updateSurvey: '/api/surveys/update/',
        surveyDetail: '/api/surveys/detail/',
        deleteSurvey: '/api/surveys/delete/',
        questionList: '/api/surveys/list/question/',
        createQuestion: '/api/surveys/create/question/',
        updateQuestion: '/api/surveys/update/question/',
        deleteQuestion: '/api/surveys/delete/question/',
        createOption: '/api/surveys/create/option/',
        updateOption: '/api/surveys/update/option/',
        deleteOption: '/api/surveys/delete/option/',
        responseSurvey: '/api/surveys/create/answer/student/',
        getResponse: '/api/surveys/responses/',
        getStudentResponse: '/api/surveys/student/res/',
        sendAlert: '/api/ai/send/alert/',
    }
}