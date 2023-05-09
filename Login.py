from flask import Flask, render_template, redirect, request, session, url_for, json, Response
import psycopg2

app = Flask(__name__)
app.secret_key = 'development'

# database connection
try:
    conn_string = "host = 'localhost' dbname = 'pc_buildup' user = 'postgres' password = 'root'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print "DataBase Successfully Connected"

    # load the default page
    @app.route('/')
    def index():
        return render_template('home.html')

    # check the session
    @app.route('/login_user')
    def login_users():
        if not session.get('logged_in'):
            return redirect(url_for('index'))
        else:
            return render_template('home.html')

    # login to the system
    @app.route('/login_user', methods=['POST'])
    def login_user():
        user_name = request.form['user_name']
        password = request.form['password']
        error = None
        sql = "select user_name, password,user_type from user_register where user_name='" + user_name + "'and password='" + password + "'"
        cursor.execute(sql)
        conn.commit()
        value = cursor.fetchall()
        if not value:
            error = 'Invalid Username or Password'
            return render_template('index.html', error=error)
        elif value:
            user_category = value[0][2].strip()
            if request.method == 'POST':
                session['logged_in'] = True
                session['user_role'] = value[0][2].strip()
                if user_category == 'Admin':
                    return render_template('home2.html')
                elif user_category == 'Builder':
                    return render_template('home6.html')
                elif user_category == 'Shop':
                    return render_template('home4.html')
                elif user_category == 'Client':
                    return render_template('home5.html')
                elif user_category == 'Deliver':
                    return render_template('home3.html')
            return render_template('error.html')

    # Client register
    @app.route('/client_register', methods=['POST'])
    def client_register():
        try:
            name = request.form['f_name']
            address = request.form['address']
            nic_number = request.form['nic']
            p_num = request.form['p_num']
            user_type = request.form['user_type']
            email = request.form['email']
            user_name = request.form['user_name']
            password = request.form['password']
            sql = """INSERT INTO user_register(client_name, address, nic, p_num, user_type, email, user_name, password) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                name,
                address,
                nic_number,
                p_num,
                user_type,
                email,
                user_name,
                password)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('client_reg'))
        except:
            print"Error"
            return redirect(url_for('error'))

    # user register
    @app.route('/user_register', methods=['POST'])
    def user_register():
        try:
            name = request.form['f_name']
            address = request.form['address']
            nic_number = request.form['nic']
            p_num = request.form['p_num']
            user_type = request.form['user_type']
            email = request.form['email']
            user_name = request.form['user_name']
            password = request.form['password']
            sql = """INSERT INTO user_register(client_name, address, nic, p_num, user_type, email, user_name, password) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                name,
                address,
                nic_number,
                p_num,
                user_type,
                email,
                user_name,
                password)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('user_reg'))
        except:
            print"Error"
            return redirect(url_for('error'))

    # Items register
    @app.route('/item_register', methods=['POST'])
    def item_register():
        try:
            item = request.form['item']
            capacity = request.form['capacity']
            number_of_items = request.form['number_of_items']
            price = request.form['price']
            date_of_store = request.form['date_of_store']

            sql = """INSERT INTO item_register(item, capacity, number_of_items, price, date_of_store) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (
                item,
                capacity,
                number_of_items,
                price,
                date_of_store)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('item_reg'))
        except:
            print"Error"
            return redirect(url_for('error'))


    # set menu pc
    @app.route('/set_menu_reg', methods=['POST'])
    def set_menu_reg():
        try:
            pc_type = request.form['pc_type']
            cpu = request.form['cpu']
            cooler = request.form['cooler']
            motherboard = request.form['motherboard']
            memory = request.form['memory']
            storage = request.form['storage']
            vga = request.form['vga']
            casing = request.form['casing']
            power = request.form['power']
            os = request.form['os']
            total = request.form['total']
            sql = """INSERT INTO set_menu(pc_type, cpu, cooler, motherboard, memory, storage, vga, casing, power, os, total) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                pc_type,
                cpu,
                cooler,
                motherboard,
                memory,
                storage,
                vga,
                casing,
                power,
                os,
                total)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('set_menu'))
        except:
            print"Error"
            return redirect(url_for('error'))


    # order  menu pc
    @app.route('/order_set_menu', methods=['POST'])
    def order_set_menu():
        try:
            pc_type = request.form['pc_type']
            cpu = request.form['cpu']
            cooler = request.form['cooler']
            motherboard = request.form['motherboard']
            memory = request.form['memory']
            storage = request.form['storage']
            vga = request.form['vga']
            casing = request.form['casing']
            power = request.form['power']
            os = request.form['os']
            total = request.form['total']
            f_name = request.form['f_name']
            nic = request.form['nic']
            address = request.form['address']
            p_number = request.form['p_number']
            payment = request.form['payment']
            operation = request.form['operation']
            sql = """INSERT INTO set_menu_orders(pc_type, cpu, cooler, motherboard, memory, storage, vga, casing, power, os, total, f_name, nic, address, p_number, payment,operation) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                pc_type,
                cpu,
                cooler,
                motherboard,
                memory,
                storage,
                vga,
                casing,
                power,
                os,
                total,
                f_name,
                nic,
                address,
                p_number,
                payment,
                operation)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('set_menu_orders'))
        except:
            print"Error"
            return redirect(url_for('error'))

    # order   delivery menu pc
    @app.route('/order_delivery', methods=['POST'])
    def order_delivery():
        try:
            pc_type = request.form['pc_type']
            cpu = request.form['cpu']
            cooler = request.form['cooler']
            motherboard = request.form['motherboard']
            memory = request.form['memory']
            storage = request.form['storage']
            vga = request.form['vga']
            casing = request.form['casing']
            power = request.form['power']
            os = request.form['os']
            total = request.form['total']
            f_name = request.form['f_name']
            nic = request.form['nic']
            address = request.form['address']
            p_number = request.form['p_number']
            payment = request.form['payment']
            delivery = request.form['delivery']
            sql = """INSERT INTO delivery_orders(pc_type, cpu, cooler, motherboard, memory, storage, vga, casing, power, os, total, f_name, nic, address, p_number, payment,delivery) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                pc_type,
                cpu,
                cooler,
                motherboard,
                memory,
                storage,
                vga,
                casing,
                power,
                os,
                total,
                f_name,
                nic,
                address,
                p_number,
                payment,
                delivery)
            cursor.execute(sql)
            conn.commit()
            print "Data Successfully added to the user table"
            return redirect(url_for('completed'))
        except:
            print"Error"
            return redirect(url_for('finish'))



                    # Show data in the table
    @app.route('/table', methods=['GET', 'POST'])
    def table():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM user_register"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('tables.html', values=values)

    # Show items in the table
    @app.route('/item', methods=['GET', 'POST'])
    def item():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM item_register"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('item_view.html', values=values)

     # Show set menu pc
    @app.route('/set_menu_orders', methods=['GET', 'POST'])
    def set_menu_orders():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM set_menu"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('order_set_menu.html', values=values)

    # Show gaming pc
    @app.route('/gaming', methods=['GET', 'POST'])
    def gaming():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM set_menu WHERE pc_type= 'gaming'"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('gaming.html', values=values)

    # Show graphic pc
    @app.route('/graphic', methods=['GET', 'POST'])
    def graphic():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM set_menu WHERE pc_type= 'graphic'"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('graphic.html', values=values)

    # Show graphic pc
    @app.route('/normal', methods=['GET', 'POST'])
    def normal():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM set_menu WHERE pc_type= 'normal'"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('normal_pc.html', values=values)

        # Show set menu orders
    @app.route('/order_list', methods=['GET', 'POST'])
    def order_list():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM set_menu_orders"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('order_list.html', values=values)

     # Show delever finish pc in the table
    @app.route('/finish', methods=['GET', 'POST'])
    def finish():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM set_menu_orders WHERE operation= 'finish'"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('delivery.html', values=values)

    # Show  finish buildup pc in the table
    @app.route('/finish_orders', methods=['GET', 'POST'])
    def finish_orders():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM set_menu_orders WHERE operation= 'finish'"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('finish_orders.html', values=values)

     # Show delivered pc in the table
    @app.route('/completed', methods=['GET', 'POST'])
    def completed():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT * FROM delivery_orders WHERE delivery= 'finish_payment'"
        cursor.execute(select_query)
        conn.commit()
        values = cursor.fetchall()
        return render_template('completed.html', values=values)

    # load data into drop down list
    @app.route('/drop_down')
    def drop_down():
        if not session.get('logged_in'):
            return render_template('index.html')
        select_query = "SELECT password ,user_name FROM user_register "
        cursor.execute(select_query)
        value = cursor.fetchall()
        return render_template('drop_down.html', values=value)


    # button action to user
    @app.route('/button_actions', methods=['POST', 'GET'])
    def button_actions():
        if request.method == 'POST' and request.form['submit'] == 'Modify':
            return modify_orders()
        elif request.method == 'POST' and request.form['submit'] == 'Delete':
            return delete_data()

    # button action to orders
    @app.route('/button_orders', methods=['POST', 'GET'])
    def button_orders():
        if request.method == 'POST' and request.form['submit'] == 'Modify':
            return modify_orders()
        elif request.method == 'POST' and request.form['submit'] == 'Delete':
            return delete_orders()

    # Delete user
    @app.route('/delete_orders', methods=['POST'])
    def delete_orders():
        id = request.form['id']
        try:
            delete_query = "DELETE FROM set_menu_orders WHERE id = '" + id + "'"
            cursor.execute(delete_query)
            conn.commit()
            print "Successfully Deleted"
            return redirect(url_for('order_list'))
        except:
            print "Error"
            return redirect(url_for('order_list'))


    # Modify Data
    @app.route('/modify_orders', methods=['POST'])
    def modify_orders():
        # get values from the form
        pc_type = request.form['pc_type']
        cpu = request.form['cpu']
        cooler = request.form['cooler']
        motherboard = request.form['motherboard']
        memory = request.form['memory']
        storage = request.form['storage']
        vga = request.form['vga']
        casing = request.form['casing']
        power = request.form['power']
        os = request.form['os']
        total = request.form['total']
        f_name = request.form['f_name']
        nic = request.form['nic']
        address = request.form['address']
        p_number = request.form['p_number']
        payment = request.form['payment']
        operation = request.form['operation']
        try:
            # update query
            update_query = "UPDATE set_menu_orders SET pc_type = '" + pc_type + "', cpu = '" + cpu + "', cooler = '" + cooler + "', motherboard = '" + motherboard + "',  memory = '" + memory + "',storage = '" + storage + "', vga = '" + vga + "', casing = '" + casing + "', power = '" + power + "',  os = '" + os + "', total = '" + total + "',  f_name = '" + f_name + "',nic = '" + nic + "', address = '" + address + "', p_number = '" + p_number + "', payment = '" + payment + "',  operation = '" + operation + "'  WHERE nic = '" + nic + "'"
            cursor.execute(update_query)
            conn.commit()
            print "Update Successful"
            return redirect(url_for('order_list'))
        except:
            print "Error"
            return redirect(url_for('order_list'))


                # Delete user
    @app.route('/delete_data', methods=['POST'])
    def delete_data():
        id = request.form['id']
        try:
            delete_query = "DELETE FROM user_register WHERE id = '" + id + "'"
            cursor.execute(delete_query)
            conn.commit()
            print "Successfully Deleted"
            return redirect(url_for('view_user'))
        except:
            print "Error"
            return redirect(url_for('table'))



    # client register
    @app.route('/client_reg')
    def client_reg():
        return render_template('index.html')

    # index page
    @app.route('/index_page')
    def index_page():
        return render_template('index.html')

    # items register
    @app.route('/item_reg')
    def item_reg():
        return render_template('items_register.html')

  #set_menu register
    @app.route('/set_menu')
    def set_menu():
        return render_template('set_menu.html')

    # customize register
    @app.route('/customise')
    def customise():
        return render_template('customise.html')

     # error
    @app.route('/error')
    def error():
        return render_template('error.html')

    # pi chart
    @app.route('/pipline')
    def pipline():
        try:
            if not session.get('logged_in'):
                return render_template('pipe.html')
            sql = "select operation vc, count(*) from set_menu_orders group by operation"
            cursor.execute(sql)
            data = cursor.fetchall()
            # return data
            return render_template('pipe.html', data=data)

        except Exception as e:
            return (str(e))

    # user register
    @app.route('/user_reg')
    def user_reg():
        return render_template('user_register.html')

    # logout from the system
    @app.route('/logout')
    def logout():
        session['logged_in'] = False
        session.pop = ['logged_in', None]
        session.clear()
        return redirect(url_for('index'))

    # clear the cache after logout
    @app.after_request
    def add_header(response):
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
        return response

    if __name__ == '__main__':
        app.run(debug=True)

except:
    print "Connection Failed"




