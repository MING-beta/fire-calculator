// js/state.js
// 애플리케이션의 전역 상태를 관리하는 객체입니다.

export const state = {
    isCompareMode: false,
    targetMode: 'life', // 'life' or 'swr'
    calcMode: 'age',    // 'age' or 'savings'
    lifeEvents: [],

    // 추가적인 상태를 이곳에 관리할 수 있습니다.
    currentProfileId: null // 프로필 관리에 사용될 수 있음
};
