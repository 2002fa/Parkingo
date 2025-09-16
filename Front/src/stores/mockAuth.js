// فایل موقت برای شبیه‌سازی store احراز هویت
export const useMockAuthStore = () => {
    return {
        user: {
            full_name: "امین رضایی",
            username: "admin",
            role: "admin"
        }
    };
};