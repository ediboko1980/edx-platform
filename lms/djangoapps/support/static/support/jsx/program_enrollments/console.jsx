import React from 'react';
import PropTypes from 'prop-types';
import Cookies from 'js-cookie';
import { Button, InputText, StatusAlert } from '@edx/paragon';

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
    {props.errors.map(errorItem => (
      <StatusAlert
        open
        dismissible={false}
        alertType="danger"
        dialog={errorItem}
      />
    ))}
    <InputText
      name="external_user_key"
      label="Institution user key from school. For example, GTPersonDirectoryId for GT students"
      value={props.learnerInfo.external_user_key}
    />
    <Button label="Submit" type="submit" className={['btn', 'btn-primary']} />
  </form>
);

ProgramEnrollmentsConsolePage.propTypes = {
  successes: PropTypes.arrayOf(PropTypes.string),
  errors: PropTypes.arrayOf(PropTypes.string),
  text: PropTypes.string,
  learnerInfo: PropTypes.object,
  orgKeys: PropTypes.arrayOf(Proptypes.string)
};

ProgramEnrollmentsConsolePage.defaultProps = {
  successes: [],
  errors: [],
  text: '',
  learnerInfo: '',
  orgKeys: [],
};
