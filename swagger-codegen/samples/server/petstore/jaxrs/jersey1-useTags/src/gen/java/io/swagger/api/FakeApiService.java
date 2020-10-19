package io.swagger.api;

import io.swagger.api.*;
import io.swagger.model.*;

import com.sun.jersey.multipart.FormDataParam;

import java.math.BigDecimal;
import io.swagger.model.Client;
import java.util.Date;
import io.swagger.model.OuterComposite;
import io.swagger.model.User;

import java.util.List;
import io.swagger.api.NotFoundException;

import java.io.InputStream;

import com.sun.jersey.core.header.FormDataContentDisposition;
import com.sun.jersey.multipart.FormDataParam;

import javax.ws.rs.core.Response;
import javax.ws.rs.core.SecurityContext;
import javax.validation.constraints.*;

public abstract class FakeApiService {
      public abstract Response fakeOuterBooleanSerialize(Boolean body,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response fakeOuterCompositeSerialize(OuterComposite body,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response fakeOuterNumberSerialize(BigDecimal body,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response fakeOuterStringSerialize(String body,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response testBodyWithQueryParams(User body, @NotNull String query,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response testClientModel(Client body,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response testEndpointParameters(BigDecimal number,Double _double,String patternWithoutDelimiter,Integer integer,Integer int32,Long int64,Float _float,String string,Date date,Date dateTime,String password,String paramCallback,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response testEnumParameters(List<String> enumHeaderStringArray,String enumHeaderString, List<String> enumQueryStringArray, String enumQueryString, Integer enumQueryInteger,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response testInlineAdditionalProperties(Object param,SecurityContext securityContext)
      throws NotFoundException;
      public abstract Response testJsonFormData(String param,String param2,SecurityContext securityContext)
      throws NotFoundException;
}
