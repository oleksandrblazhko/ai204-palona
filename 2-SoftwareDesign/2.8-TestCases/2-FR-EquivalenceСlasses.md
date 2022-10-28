
<table>
    <thead align="center">
        <tr>
            <td>Опис вхідних умов</td>
            <td>Правильний/неправильний клас еквівалентності</td>
            <td>Опис значень вхідних даних</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
              <ol>
                <li>Рядок <i>aname</i> <b>починається</b> з літери</li>
            <li>Довжина рядка <i>aname</i> має <b>не більше</b> 15 символів</li>
            <li>Рядок <i>abirthday</i> <b>має</b> формат "День.Місяць.Рік"</li>
            <li>Рядок <i>aphonenumber</i> <b>починається</b> з +</li>
            <li>Рядок <i>aphonenumber</i> <b>містить</b> 13 символів</li>
            <li>Рядок <i>ae-mail</i> <b>має</b> формат "Ім'яПоштовоїСкриньки@доменнеІм'яСервера"</li>
              </ol>
            </td>
            <td align="center">Правильний</td>
          <td>
            <i>
            <br>aname = Matvii</br>
            <br>abirthday = 28.11.2002</br>
            <br>aphonenumber = +380954841270</br>
            <br>ae-mail = matvii122@gmail.com</br>
            </i>
          </td>
        </tr>
        <tr>
             <td>
              <ol>
            <li>Рядок <i>aname</i> <b>не починається</b> з літери</li>
            <li>Довжина рядка <i>aname</i> має не більше 15 символів</li>
            <li>Рядок <i>abirthday</i> повинен мати формат "День.Місяць.Рік"</li>
            <li>Рядок <i>aphonenumber</i> починається з +</li>
            <li>Рядок <i>aphonenumber</i> повинен містити 13 символів</li>
            <li>Рядок <i>ae-mail</i> повинен мати формат "Ім'яПоштовоїСкриньки@доменнеІм'яСервера"</li>
              </ol>
            </td>
            <td align="center">Неправильний</td>
          <td>
            <i>
            <br>aname = 2atvii</br>
            <br>abirthday = 28.11.2002</br>
            <br>aphonenumber = +380954841270</br>
            <br>ae-mail = matvii122@gmail.com</br>
            </i>
          </td>
        </tr>
        <tr>
             <td>
              <ol>
            <li>Рядок <i>aname</i> починається з літери</li>
            <li>Довжина рядка <i>aname</i> <b>має більше</b> 15 символів</li>
            <li>Рядок <i>abirthday</i> повинен мати формат "День.Місяць.Рік"</li>
            <li>Рядок <i>aphonenumber</i> починається з +</li>
            <li>Рядок <i>aphonenumber</i> повинен містити 13 символів</li>
            <li>Рядок <i>ae-mail</i> повинен мати формат "Ім'яПоштовоїСкриньки@доменнеІм'яСервера"</li>
              </ol>
            </td>
            <td align="center">Неправильний</td>
          <td>
            <i>
            <br>aname = Maааааааааааtviiіі</br>
            <br>abirthday = 28.11.2002</br>
            <br>aphonenumber = +380954841270</br>
            <br>ae-mail = matvii122@gmail.com</br>
            </i>
          </td>
        </tr>
        <tr>
             <td>
              <ol>
                <li>Рядок <i>aname</i> починається з літери</li>
            <li>Довжина рядка <i>aname</i> має не більше 15 символів</li>
            <li>Рядок <i>abirthday</i> <b>не має</b> формат "День.Місяць.Рік"</li>
            <li>Рядок <i>aphonenumber</i> починається з +</li>
            <li>Рядок <i>aphonenumber</i> містить 13 символів</li>
            <li>Рядок <i>ae-mail</i> має формат "Ім'яПоштовоїСкриньки@доменнеІм'яСервера"</li>
              </ol>
            </td>
            <td align="center">Неправильний</td>
          <td>
            <i>
            <br>aname = Matvii</br>
            <br>abirthday = Двадцять восьме.11.2002</br>
            <br>aphonenumber = +380954841270</br>
            <br>ae-mail = matvii122@gmail.com</br>
            </i>
          </td>
        </tr>
        <tr>
             <td>
              <ol>
            <li>Рядок <i>aname</i> починається з літери</li>
            <li>Довжина рядка <i>aname</i> має не більше 15 символів</li>
            <li>Рядок <i>abirthday</i> має формат "День.Місяць.Рік"</li>
            <li>Рядок <i>aphonenumber</i> <b>не починається</b> з +</li>
            <li>Рядок <i>aphonenumber</i> містить 13 символів</li>
            <li>Рядок <i>ae-mail</i> має формат "Ім'яПоштовоїСкриньки@доменнеІм'яСервера"</li>
              </ol>
            </td>
            <td align="center">Неправильний</td>
          <td>
            <i>
            <br>aname = Matvii</br>
            <br>abirthday = 28.11.2002</br>
            <br>aphonenumber = 3380954841270</br>
            <br>ae-mail = matvii122@gmail.com</br>
            </i>
          </td>
        </tr>
        <tr>
            <td>
              <ol>
            <li>Рядок <i>aname</i> починається з літери</li>
            <li>Довжина рядка <i>aname</i> має не більше 15 символів</li>
            <li>Рядок <i>abirthday</i> має формат "День.Місяць.Рік"</li>
            <li>Рядок <i>aphonenumber</i> починається з +</li>
            <li>Рядок <i>aphonenumber</i> <b>не містить</b> 13 символів</li>
            <li>Рядок <i>ae-mail</i> має формат "Ім'яПоштовоїСкриньки@доменнеІм'яСервера"</li>
              </ol>
            </td>
            <td align="center">Неправильний</td>
          <td>
            <i>
            <br>aname = Matvii</br>
            <br>abirthday = 28.11.2002</br>
            <br>aphonenumber = +380954841270000</br>
            <br>ae-mail = matvii122@gmail.com</br>
            </i>
          </td>
        </tr>
        <tr>
            <td>
              <ol>
            <li>Рядок <i>aname</i> починається з літери</li>
            <li>Довжина рядка <i>aname</i> має не більше 15 символів</li>
            <li>Рядок <i>abirthday</i> має формат "День.Місяць.Рік"</li>
            <li>Рядок <i>aphonenumber</i> починається з +</li>
            <li>Рядок <i>aphonenumber</i> містить 13 символів</li>
            <li>Рядок <i>ae-mail</i> <b>не має</b> формат "Ім'яПоштовоїСкриньки@доменнеІм'яСервера"</li>
              </ol>
            </td>
            <td align="center">Неправильний</td>
          <td>
            <i>
            <br>aname = Matvii</br>
            <br>abirthday = 28.11.2002</br>
            <br>aphonenumber = +380954841270000</br>
            <br>ae-mail = matvii122gmail.com</br>
            </i>
          </td>
        </tr>
    </tbody>
</table>
