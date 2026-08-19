// 游戏代码
function startPuzzle() {
            // 获取图片堆放区域
            let stack = document.getElementById("puzzleStack");
            // 清空之前的图片
            stack.innerHTML = "";
            // 七张图片
            let images = [
                "map1.png",
                "map2.png",
                "map3.png",
                "map4.png",
                "map5.png",
                "map6.png",
                "map7.png"
            ];
            // 随机打乱图片顺序
            for (let i = images.length - 1; i > 0; i--) {
                let j = Math.floor(Math.random() * (i + 1));
                [images[i], images[j]] = [images[j], images[i]];
            }
            // 循环生成图片
            images.forEach(function (img, index) {
                let piece = document.createElement("img");
                piece.src = "/static/games/images/" + img;
                piece.className = "puzzle-piece";
                // 所有图片中心完全重合
                piece.style.left = "50%";
                piece.style.top = "50%";
                // 随机旋转
                let rotate = Math.random() * 20 - 10;
                piece.style.transform =
                    "translate(-50%, -50%) rotate(" + rotate + "deg)";
                // 随机上下顺序
                piece.style.zIndex = index;
                stack.appendChild(piece);
            });
        }
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
