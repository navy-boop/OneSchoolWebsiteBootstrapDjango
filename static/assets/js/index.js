// 游戏代码

// 注册代码
console.log("注册 JavaScript 已加载");
        document.getElementById("registerForm").addEventListener("submit", function (event) {
            console.log("点击了立即注册");
            // 阻止表单默认提交
            event.preventDefault();
            const form = this;
            const usernameError = document.getElementById("usernameError");
            const passwordError = document.getElementById("passwordError");
            // 获取用户名输入框
            const usernameInput = document.querySelector('input[name="username"]');
            // 获取两个密码输入框
            const password1Input = document.querySelector('input[name="password1"]');
            const password2Input = document.querySelector('input[name="password2"]');
            // 用户开始修改用户名时，清除用户名错误信息
            usernameInput.addEventListener("input", function () {
                usernameError.textContent = "";
            });
            // 用户开始修改设置密码时，清除密码错误信息
            password1Input.addEventListener("input", function () {
                passwordError.textContent = "";
            });
            // 用户开始修改确认密码时，清除密码错误信息
            password2Input.addEventListener("input", function () {
                passwordError.textContent = "";
            });
            console.log("usernameError:", usernameError);
            console.log("passwordError:", passwordError);
            // 清除之前的错误信息
            usernameError.textContent = "";
            passwordError.textContent = "";
            fetch(form.action, {
                method: "POST",
                body: new FormData(form)
            })
                .then(response => {
                    console.log("服务器状态：", response.status);
                    return response.json();
                })
                .then(data => {
                    console.log("服务器返回：", data);
                    if (data.success) {
                        console.log("注册成功");
                        window.location.href = data.redirect;
                    } else {
                        console.log("注册失败，错误信息：", data.errors);
                        // 用户名错误
                        if (data.errors && data.errors.username) {
                            usernameError.textContent = data.errors.username;
                        }
                        // 密码错误
                        if (data.errors && data.errors.password) {
                            passwordError.textContent = data.errors.password;
                        }
                    }
                })
                .catch(error => {
                    console.error("注册请求错误：", error);
                });
        });
