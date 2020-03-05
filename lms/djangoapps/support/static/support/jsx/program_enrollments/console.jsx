import React from 'react';
import PropTypes from 'prop-types';
import Cookies from 'js-cookie';
import { Button, InputText, StatusAlert, InputSelect } from '@edx/paragon';

export const ProgramEnrollmentsConsolePage = props => (
  <form method="post">
    <input type="hidden" name="csrfmiddlewaretoken" value={Cookies.get('csrftoken')} />
    {props.successes.length > 0 && (
      <StatusAlert
        open
        alertType="success"
        dialog={(
          <div>
            <span></span>
          </div>
        )}
      />
    )}
    <div key="edX_accounts">
      <InputText
        name="edx_user"
        label="edX account username or email"
        value={props.learnerInfo}
      />
    </div>
    <div key="school_accounts">
      <InputSelect
        name="IdPSelect"
        label="Learner Account Providers"
        value="Select One"
        options={
          props.orgKeys
        }
      />

      <InputText
        name="external_user_key"
        label="Institution user key from school. For example, GTPersonDirectoryId for GT students"
        value={props.learnerInfo}
      />
    </div>
    <Button label="Search" type="submit" className={['btn', 'btn-primary']} />
  </form>
);

ProgramEnrollmentsConsolePage.propTypes = {
  successes: PropTypes.arrayOf(PropTypes.string),
  errors: PropTypes.arrayOf(PropTypes.string),
  learnerInfo: PropTypes.string,
  orgKeys: PropTypes.arrayOf(PropTypes.object),
};

ProgramEnrollmentsConsolePage.defaultProps = {
  successes: [],
  errors: [],
  learnerInfo: '',
  orgKeys: [],
};
