from flask import Flask, render_template, request

app = Flask('my web')


@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')

    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        more = request.form.get("more")
        print(user, pwd, gender, hobby_list, city, more)
        # 将用户信息写入文件中实现注册、写入到excel中实现注册、写入数据库中实现注册

        # 2.给用户再返回结果
        return "注册成功"


if __name__ == '__main__':
    app.run()